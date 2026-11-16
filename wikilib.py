"""共用函式：讀取 wiki 頁面、簡報原始檔，供 build.py 與 check.py 使用。

只依賴 PyYAML。所有路徑都以專案根目錄為基準。
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SLIDES = ROOT / "slides"
SITE = ROOT / "site"
DOCS = ROOT / "docs"

WIKILINK = re.compile(r"\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]")
SLIDE_META = re.compile(r"<!--\s*(.*?)\s*-->", re.S)
SPECIAL = {"index", "log"}  # wiki/index.md 與 wiki/log.md 不是一般頁面


def split_frontmatter(text: str) -> tuple[dict, str]:
    """回傳 (frontmatter dict, 內文)。沒有 frontmatter 時回傳空 dict。"""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            try:
                meta = yaml.safe_load(text[4:end]) or {}
            except yaml.YAMLError as e:  # 不要讓整個檢查當掉，交給 W0 回報
                meta = {"_yaml_error": str(e).splitlines()[0]}
            if not isinstance(meta, dict):
                meta = {"_yaml_error": "frontmatter 不是 key: value 的形式"}
            return meta, text[end + 5:].lstrip("\n")
    return {}, text


@dataclass
class Page:
    slug: str
    path: Path
    meta: dict
    body: str

    @property
    def type(self) -> str:
        return self.meta.get("type", "")

    @property
    def title(self) -> str:
        return self.meta.get("title", self.slug)

    def links(self) -> list[str]:
        return [m.group(1) for m in WIKILINK.finditer(self.body)]

    def sections(self) -> list[tuple[str, str]]:
        """以 H2 切段，回傳 [(標題, 內容)]；H2 之前的前言標題為空字串。"""
        parts = re.split(r"^## +(.+)$", self.body, flags=re.M)
        out = [("", parts[0])]
        for i in range(1, len(parts), 2):
            out.append((parts[i].strip(), parts[i + 1]))
        return out


def load_pages() -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for path in sorted(WIKI.rglob("*.md")):
        if path.parent == WIKI and path.stem in SPECIAL:
            continue
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        slug = path.stem
        if slug in pages:
            raise SystemExit(f"slug 重複：{slug}（{path} 與 {pages[slug].path}）")
        pages[slug] = Page(slug, path, meta, body)
    return pages


@dataclass
class Slide:
    number: int
    layout: str
    refs: list[str]
    body: str


@dataclass
class Deck:
    name: str
    path: Path
    meta: dict
    slides: list[Slide] = field(default_factory=list)


def load_decks() -> list[Deck]:
    decks = []
    for path in sorted(SLIDES.glob("*/deck.md")):
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        deck = Deck(path.parent.name, path, meta)
        chunks = [c.strip() for c in re.split(r"^---\s*$", body, flags=re.M)]
        for n, chunk in enumerate([c for c in chunks if c], start=1):
            layout, refs = "bullets", []
            m = SLIDE_META.match(chunk)
            if m:
                for item in m.group(1).split("|"):
                    if ":" in item:
                        key, value = item.split(":", 1)
                        key, value = key.strip(), value.strip()
                        if key == "layout":
                            layout = value
                        elif key == "refs":
                            refs = [r.strip() for r in value.split(",") if r.strip()]
                chunk = chunk[m.end():].strip()
            deck.slides.append(Slide(n, layout, refs, chunk))
        decks.append(deck)
    return decks


def plain_text(md_text: str) -> str:
    """把 markdown 粗略轉成純文字，用於數字比對。"""
    text = WIKILINK.sub(lambda m: m.group(2) or m.group(1), md_text)
    text = re.sub(r"\{\{diagram:[a-z0-9-]+\}\}", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text
