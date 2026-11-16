"""建置腳本：把 wiki/ 與 slides/ 轉成 docs/ 底下的靜態網站（GitHub Pages 讀 docs/）。

用法：
    python tools/build.py

docs/ 是產出物，每次建置都會整個重寫，請不要手動編輯 docs/ 裡的檔案。
需要的套件：markdown、jinja2、pyyaml。
"""
from __future__ import annotations

import re
import shutil

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from wikilib import DOCS, ROOT, SITE, WIKI, WIKILINK, load_decks, load_pages, split_frontmatter

MD_EXT = ["tables", "fenced_code", "attr_list", "sane_lists"]
DIAGRAM = re.compile(r"^\{\{diagram:([a-z0-9-]+)\}\}\s*$", re.M)
TYPE_LABEL = {"concept": "概念", "source": "來源", "meta": "關於本站", "discussion": "討論紀錄"}


def load_config() -> dict:
    return yaml.safe_load((SITE / "config.yml").read_text(encoding="utf-8"))


def render_md(text: str, pages: dict, wiki_prefix: str) -> str:
    """markdown → HTML。wiki_prefix 是從輸出頁面到 docs/wiki/ 的相對路徑。"""

    def link(m: re.Match) -> str:
        slug, label = m.group(1), m.group(2)
        page = pages.get(slug)
        if page is None:
            return f'<span class="broken-link">{label or slug}</span>'
        href = f"{wiki_prefix}{slug}.html"
        if slug.startswith("src-") and not label:
            return f'<a class="cite" href="{href}" title="{page.title}">{page.meta.get("short", slug)}</a>'
        return f'<a href="{href}">{label or page.title}</a>'

    def diagram(m: re.Match) -> str:
        path = SITE / "assets" / "diagrams" / f"{m.group(1)}.svg"
        if not path.exists():
            return f'<p class="broken-link">找不到圖：{m.group(1)}</p>'
        svg = "".join(line.strip() + " " for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
        # 同一頁可能有多張圖：把 id 加上圖名前綴，避免箭頭參照到另一張（可能被隱藏的）圖
        svg = re.sub(r'id="([\w-]+)"', rf'id="{m.group(1)}-\1"', svg)
        svg = re.sub(r"url\(#([\w-]+)\)", rf"url(#{m.group(1)}-\1)", svg)
        return f'\n<figure class="diagram">{svg}</figure>\n'

    text = DIAGRAM.sub(diagram, text)
    text = WIKILINK.sub(link, text)
    return markdown.markdown(text, extensions=MD_EXT)


def main():
    cfg = load_config()
    pages = load_pages()
    decks = load_decks()
    env = Environment(
        loader=FileSystemLoader(SITE / "templates"),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "wiki").mkdir(parents=True)
    shutil.copytree(SITE / "assets", DOCS / "assets", ignore=shutil.ignore_patterns("diagrams"))
    (DOCS / ".nojekyll").write_text("不要用 Jekyll 處理這個資料夾\n", encoding="utf-8")

    # 反向連結、被哪幾張投影片引用
    backlinks: dict[str, list] = {s: [] for s in pages}
    for p in pages.values():
        for target in dict.fromkeys(p.links()):
            if target in pages and target != p.slug and p.type != "discussion":
                backlinks[target].append(p)
    in_slides: dict[str, list] = {s: [] for s in pages}
    for deck in decks:
        for s in deck.slides:
            for ref in s.refs:
                if ref in in_slides:
                    in_slides[ref].append({"deck": deck, "number": s.number})

    path_slugs = [s for s in cfg.get("learning_path", []) if s in pages]
    common = {"cfg": cfg, "type_label": TYPE_LABEL, "decks": decks}

    # ---- wiki 各頁
    tpl = env.get_template("page.html")
    for p in pages.values():
        prev_p = next_p = None
        if p.slug in path_slugs:
            i = path_slugs.index(p.slug)
            prev_p = pages[path_slugs[i - 1]] if i > 0 else None
            next_p = pages[path_slugs[i + 1]] if i + 1 < len(path_slugs) else None
        html = tpl.render(
            **common, root="../", page=p, body=render_md(p.body, pages, ""),
            sources=[pages[s] for s in (p.meta.get("sources") or []) if s in pages],
            backlinks=sorted(backlinks[p.slug], key=lambda x: x.title),
            in_slides=in_slides[p.slug], prev=prev_p, next=next_p,
            step=(path_slugs.index(p.slug) + 1) if p.slug in path_slugs else None,
            steps=len(path_slugs),
        )
        (DOCS / "wiki" / f"{p.slug}.html").write_text(html, encoding="utf-8")

    # ---- index.md 與 log.md
    tpl = env.get_template("plain.html")
    for name, title in (("index", "Wiki 目錄"), ("log", "更新紀錄")):
        _, body = split_frontmatter((WIKI / f"{name}.md").read_text(encoding="utf-8"))
        body = re.sub(r"^# .+\n", "", body, count=1)
        html = tpl.render(**common, root="../", title=title, kind=name, body=render_md(body, pages, ""))
        out = "catalog.html" if name == "index" else "log.html"
        (DOCS / "wiki" / out).write_text(html, encoding="utf-8")

    # ---- 首頁
    groups = []
    for g in cfg.get("groups", []):
        members = sorted(
            (p for p in pages.values() if p.type == "concept" and p.meta.get("group") == g["name"]),
            key=lambda x: (path_slugs.index(x.slug) if x.slug in path_slugs else 99, x.title),
        )
        if members:
            groups.append({"name": g["name"], "blurb": g.get("blurb", ""), "pages": members})
    html = env.get_template("home.html").render(
        **common, root="", groups=groups,
        path=[pages[s] for s in path_slugs],
        sources=sorted((p for p in pages.values() if p.type == "source"), key=lambda x: str(x.meta.get("published", ""))),
        meta_pages=[p for p in pages.values() if p.type == "meta"],
        counts={"concept": sum(p.type == "concept" for p in pages.values()),
                "source": sum(p.type == "source" for p in pages.values()),
                "slides": sum(len(d.slides) for d in decks)},
    )
    (DOCS / "index.html").write_text(html, encoding="utf-8")

    # ---- 簡報
    tpl = env.get_template("deck.html")
    for deck in decks:
        out = DOCS / "slides" / deck.name
        out.mkdir(parents=True)
        slides = [
            {"number": s.number, "layout": s.layout, "html": render_md(s.body, pages, "../../wiki/"),
             "refs": [pages[r] for r in s.refs if r in pages]}
            for s in deck.slides
        ]
        html = tpl.render(**common, root="../../", deck=deck, slides=slides)
        (out / "index.html").write_text(html, encoding="utf-8")

    print(f"已建置 {len(pages)} 個 wiki 頁、{len(decks)} 份簡報 → {DOCS.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
