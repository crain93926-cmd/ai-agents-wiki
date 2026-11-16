"""檢查腳本：把「檢查」做成可以重複執行的節點。

用法：
    python tools/check.py wiki     # 節點 4：Wiki lint（寫完 wiki 就跑）
    python tools/check.py deck     # 節點 6：簡報大綱檢查（render 之前跑）
    python tools/check.py site     # 節點 8：產出檢查（build 之後跑）
    python tools/check.py all      # 依序全部執行

每次執行都會把結果附加到 checks/check-log.md，作為檢查紀錄。
任何一條規則失敗，程式會以非 0 結束碼離開。
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from wikilib import DOCS, RAW, ROOT, SITE, WIKI, load_decks, load_pages, plain_text

LOG = ROOT / "checks" / "check-log.md"
REQUIRED = ["title", "type", "summary", "updated"]
TYPES = {"concept", "source", "meta", "discussion"}
SKIP_SECTIONS = {"相關頁面", "延伸閱讀"}  # 這些段落不需要引用來源
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?%?")
DIAGRAM = re.compile(r"\{\{diagram:([a-z0-9-]+)\}\}")


class Report:
    def __init__(self, stage: str):
        self.stage = stage
        self.errors: list[str] = []
        self.notes: list[str] = []

    def error(self, rule: str, msg: str):
        self.errors.append(f"[{rule}] {msg}")

    def note(self, msg: str):
        self.notes.append(msg)


# ---------------------------------------------------------------- wiki lint
def check_wiki() -> Report:
    r = Report("wiki")
    pages = load_pages()
    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    log_text = (WIKI / "log.md").read_text(encoding="utf-8") if (WIKI / "log.md").exists() else ""
    inbound: dict[str, set[str]] = {s: set() for s in pages}

    for slug, p in pages.items():
        # W0 frontmatter 的 YAML 要能解析（常見原因：值裡有半形冒號卻沒加引號）
        if "_yaml_error" in p.meta:
            r.error("W0", f"{slug}: frontmatter 無法解析（{p.meta['_yaml_error']}）。值裡有半形冒號時要用引號包起來")
            continue
        # W1 frontmatter
        for key in REQUIRED:
            if not p.meta.get(key):
                r.error("W1", f"{slug}: frontmatter 缺少 {key}")
        if p.type and p.type not in TYPES:
            r.error("W1", f"{slug}: type「{p.type}」不在 {sorted(TYPES)}")
        # W3 連結都要存在
        for target in dict.fromkeys(p.links()):  # 同一個連結只回報一次
            if target not in pages:
                r.error("W3", f"{slug}: 連到不存在的頁面 [[{target}]]")
            elif target != slug:
                inbound[target].add(slug)
        # W2 來源頁必須指向 raw 檔與原始網址
        if p.type == "source":
            if not slug.startswith("src-"):
                r.error("W2", f"{slug}: 來源頁檔名必須以 src- 開頭")
            raw = p.meta.get("raw")
            if not raw or not (ROOT / raw).exists():
                r.error("W2", f"{slug}: raw 欄位指向的檔案不存在（{raw}）")
            if not str(p.meta.get("url", "")).startswith("http"):
                r.error("W2", f"{slug}: 缺少原始網址 url")
            if not p.meta.get("short"):
                r.error("W2", f"{slug}: 缺少引用簡稱 short")
            # W7 每個來源都要有 ingest 紀錄
            if f"ingest | {slug}" not in log_text:
                r.error("W7", f"{slug}: log.md 沒有對應的 ingest 紀錄")
        # W6 概念頁：每個 H2 段落都要引用來源，且與 frontmatter 一致
        if p.type == "concept":
            declared = set(p.meta.get("sources") or [])
            if not declared:
                r.error("W6", f"{slug}: 概念頁的 sources 不可為空")
            cited = {t for t in p.links() if t.startswith("src-")}
            for title, text in p.sections():
                if not title or title in SKIP_SECTIONS:
                    continue
                if not any(t.startswith("src-") for t in re.findall(r"\[\[([a-z0-9-]+)", text)):
                    r.error("W6", f"{slug}: 段落「{title}」沒有引用任何來源")
            for s in sorted(declared - cited):
                r.error("W6", f"{slug}: sources 列了 {s}，內文卻沒有引用")
            for s in sorted(cited - declared):
                r.error("W6", f"{slug}: 內文引用了 {s}，但 sources 沒有列")
            for s in sorted(declared):
                if s not in pages or pages[s].type != "source":
                    r.error("W2", f"{slug}: sources 中的 {s} 不是存在的來源頁")
        # W9 引用的圖必須存在（建置時不會報錯，只會在頁面上留下「找不到圖」）
        for name in dict.fromkeys(DIAGRAM.findall(p.body)):
            if not (SITE / "assets" / "diagrams" / f"{name}.svg").exists():
                r.error("W9", f"{slug}: 找不到圖 site/assets/diagrams/{name}.svg")
        # W5 index.md 必須列出每一頁，而且只列一次
        count = len(re.findall(rf"\[\[{re.escape(slug)}(?:\||\]\])", index_text))
        if count == 0:
            r.error("W5", f"{slug}: index.md 沒有列出這一頁")
        elif count > 1:
            r.error("W5", f"{slug}: index.md 重複列出 {count} 次")

    # W3 index.md 自己的連結
    for target in re.findall(r"\[\[([a-z0-9-]+)", index_text):
        if target not in pages:
            r.error("W3", f"index.md: 連到不存在的頁面 [[{target}]]")
    # W4 孤兒頁（除了 index 之外沒有任何頁面連過來）
    for slug, sources in inbound.items():
        if not sources and pages[slug].type in {"concept", "source"}:
            r.error("W4", f"{slug}: 孤兒頁，沒有其他頁面連到它")
    # W8 raw 檔必須有來源卡必要欄位
    for path in sorted(RAW.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for key in ("url:", "fetched:", "title:"):
            if key not in text.split("\n---\n")[0]:
                r.error("W8", f"raw/{path.name}: 來源卡缺少 {key[:-1]}")

    kinds = {}
    for p in pages.values():
        kinds[p.type] = kinds.get(p.type, 0) + 1
    r.note("頁面數：" + "、".join(f"{k} {v}" for k, v in sorted(kinds.items())))
    return r


# --------------------------------------------------------------- deck check
def check_deck() -> Report:
    r = Report("deck")
    pages = load_pages()
    decks = load_decks()
    if not decks:
        r.error("D0", "slides/ 底下沒有任何 deck.md")
    for deck in decks:
        name = deck.name
        for key in ("title", "audience", "goal"):
            if not deck.meta.get(key):
                r.error("D0", f"{name}: deck.md frontmatter 缺少 {key}")
        n = len(deck.slides)
        if not 10 <= n <= 24:
            r.error("D2", f"{name}: 投影片 {n} 張，應在 10–24 張之間")
        layouts = [s.layout for s in deck.slides]
        for needed, label in (("objectives", "學習目標"), ("quiz", "小測驗"), ("recap", "重點回顧")):
            if needed not in layouts:
                r.error("D2", f"{name}: 缺少「{label}」頁（layout: {needed}）")
        if layouts and layouts[0] != "title":
            r.error("D2", f"{name}: 第 1 張必須是 layout: title")
        used: set[str] = set()
        for s in deck.slides:
            # D1 每張都要標明出自哪些 wiki 頁
            if s.layout != "title" and not s.refs:
                r.error("D1", f"{name} 第 {s.number} 張：沒有 refs（不知道內容出自哪一頁 wiki）")
            for ref in s.refs:
                if ref not in pages:
                    r.error("D1", f"{name} 第 {s.number} 張：refs 指向不存在的頁面 {ref}")
                else:
                    used.add(ref)
            # D3 投影片上的數字必須能在所引用的 wiki 頁找到
            ref_text = " ".join(
                plain_text(pages[x].body) + " " + str(pages[x].meta) for x in s.refs if x in pages
            ).replace(",", "")
            for token in NUMBER.findall(plain_text(s.body)):
                digits = token.replace(",", "")
                if len(digits.rstrip("%")) < 2 and not digits.endswith("%"):
                    continue  # 個位數（清單編號、「三個零件」之類）不檢查
                if digits not in ref_text:
                    r.error("D3", f"{name} 第 {s.number} 張：數字「{token}」在引用的 wiki 頁中找不到")
            # D6 引用的圖必須存在
            for dname in dict.fromkeys(DIAGRAM.findall(s.body)):
                if not (SITE / "assets" / "diagrams" / f"{dname}.svg").exists():
                    r.error("D6", f"{name} 第 {s.number} 張：找不到圖 site/assets/diagrams/{dname}.svg")
            # D5 每張投影片的文字量上限（避免塞爆版面）
            length = len(re.sub(r"\s+", "", plain_text(s.body)))
            if length > 330:
                r.error("D5", f"{name} 第 {s.number} 張：文字 {length} 字，超過上限 330")
        # D4 標記為核心的概念頁一定要被簡報用到
        scope = deck.meta.get("wiki_scope") or []
        for slug in scope:
            if slug not in pages:
                r.error("D4", f"{name}: wiki_scope 中的 {slug} 不存在")
            elif slug not in used:
                r.error("D4", f"{name}: 核心頁 {slug} 沒有被任何一張投影片引用")
        r.note(f"{name}：{n} 張投影片，引用 {len(used)} 個 wiki 頁")
    return r


# --------------------------------------------------------------- site check
class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []
        self.slides = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "link") and a.get("href"):
            self.hrefs.append(a["href"])
        if tag in ("script", "img") and a.get("src"):
            self.hrefs.append(a["src"])
        if tag == "section" and "slide" in (a.get("class") or "").split():
            self.slides += 1


def check_site() -> Report:
    r = Report("site")
    html_files = sorted(DOCS.rglob("*.html"))
    if not html_files:
        r.error("S0", "docs/ 沒有任何 HTML，請先執行 python tools/build.py")
        return r
    pages = load_pages()
    decks = load_decks()
    # S4 每個 wiki 頁都要有對應的 HTML
    for slug in pages:
        if not (DOCS / "wiki" / f"{slug}.html").exists():
            r.error("S4", f"docs/wiki/{slug}.html 不存在（忘了重新 build？）")
    checked = 0
    broken: dict[str, list[str]] = {}  # 壞掉的目標 → 哪些頁面連過去（同一個原因只報一次）
    for f in html_files:
        text = f.read_text(encoding="utf-8")
        parser = _Links()
        parser.feed(text)
        # S5 建置時留下的錯誤記號（不存在的 wiki 連結或圖）
        if 'class="broken-link"' in text:
            r.error("S5", f"{f.relative_to(DOCS)}: 頁面上有「找不到」的連結或圖")
        for href in parser.hrefs:
            if re.match(r"^(https?:|mailto:|#|data:|javascript:)", href):
                continue
            target = (f.parent / href.split("#")[0].split("?")[0]).resolve()
            if target.is_dir():
                target = target / "index.html"
            checked += 1
            if not target.exists():
                key = str(target.relative_to(DOCS.resolve())) if DOCS.resolve() in target.parents else href
                broken.setdefault(key, []).append(str(f.relative_to(DOCS)))
        # S3 簡報張數要和 deck.md 一致
        for deck in decks:
            if f == DOCS / "slides" / deck.name / "index.html" and parser.slides != len(deck.slides):
                r.error("S3", f"{deck.name}: HTML 有 {parser.slides} 張，deck.md 有 {len(deck.slides)} 張")
    for key, froms in sorted(broken.items()):
        sample = "、".join(froms[:3]) + ("…" if len(froms) > 3 else "")
        r.error("S1", f"{len(froms)} 個頁面連到不存在的 {key}（{sample}）")
    r.note(f"檢查了 {len(html_files)} 個 HTML、{checked} 個站內連結")

    # S2 投影片內容不可超出版面（需要 Playwright；沒有安裝就略過並註記）
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        r.note("S2 略過：未安裝 Playwright，無法自動檢查投影片是否超出版面")
        return r
    try:
        with sync_playwright() as pw:
            try:
                browser = pw.chromium.launch()
            except Exception:
                browser = pw.chromium.launch(channel="chrome")
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            for deck in decks:
                f = DOCS / "slides" / deck.name / "index.html"
                if not f.exists():
                    r.error("S4", f"docs/slides/{deck.name}/index.html 不存在")
                    continue
                page.goto(f.as_uri())
                page.wait_for_timeout(300)
                results = page.evaluate(
                    """() => [...document.querySelectorAll('section.slide')].map((s, i) => {
                        window.__deck.go(i);
                        const inner = s.querySelector('.slide-inner');
                        const foot = s.querySelector('.slide-foot');
                        const no = s.querySelector('.foot-no');
                        return {n: i + 1, over: inner.scrollHeight - inner.clientHeight,
                                wide: inner.scrollWidth - inner.clientWidth,
                                foot: Math.max(foot.scrollHeight - foot.clientHeight, no.offsetHeight - 24)};
                    })"""
                )
                bad = [x for x in results if x["over"] > 2 or x["wide"] > 2 or x["foot"] > 2]
                for x in bad:
                    if x["foot"] > 2:
                        r.error("S2", f"{deck.name} 第 {x['n']} 張：頁尾的出處標籤太多，把頁碼擠到換行")
                    else:
                        r.error("S2", f"{deck.name} 第 {x['n']} 張：內容超出版面（高 +{x['over']}px、寬 +{x['wide']}px）")
                r.note(f"S2 {deck.name}：以 1280×720 量測 {len(results)} 張，超出版面 {len(bad)} 張")
            browser.close()
    except Exception as e:  # 瀏覽器啟動失敗不算內容錯誤，但要留下紀錄
        r.note(f"S2 略過：瀏覽器無法啟動（{type(e).__name__}: {str(e)[:80]}）")
    return r


STAGES = {"wiki": check_wiki, "deck": check_deck, "site": check_site}


def write_log(reports: list[Report], label: str):
    LOG.parent.mkdir(exist_ok=True)
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    if not LOG.exists():
        lines += ["# 檢查紀錄", "", "由 `tools/check.py` 自動附加，請勿手動修改既有紀錄。", ""]
    for rep in reports:
        status = "PASS" if not rep.errors else f"FAIL（{len(rep.errors)} 項）"
        lines.append(f"## [{now}] {rep.stage} | {status}" + (f" | {label}" if label else ""))
        lines.append("")
        for n in rep.notes:
            lines.append(f"- 備註：{n}")
        for e in rep.errors:
            lines.append(f"- ✗ {e}")
        if not rep.errors:
            lines.append("- ✓ 所有規則通過")
        lines.append("")
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    label = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--label=")), "")
    stage = args[0] if args else "all"
    names = list(STAGES) if stage == "all" else [stage]
    if any(n not in STAGES for n in names):
        raise SystemExit(__doc__)
    reports = [STAGES[n]() for n in names]
    write_log(reports, label)
    failed = False
    for rep in reports:
        print(f"== {rep.stage}: {'PASS' if not rep.errors else 'FAIL'}")
        for n in rep.notes:
            print(f"   · {n}")
        for e in rep.errors:
            print(f"   ✗ {e}")
        failed = failed or bool(rep.errors)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
