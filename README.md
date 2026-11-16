# Agent 筆記本

從零看懂 AI Agents 的學習筆記網站，加上一份由筆記產生的教學簡報。
內容用「LLM Wiki」方法維護：人挑資料、決定方向；AI 依照 [`AGENTS.md`](AGENTS.md) 讀資料、寫 Wiki、跑檢查、產生簡報。

- 網站：https://crain93926-cmd.github.io/ai-agents-wiki/
- 教學簡報：網站首頁的「看教學簡報」，或 `docs/slides/ai-agents-101/`
- 給 AI 的規則：[`AGENTS.md`](AGENTS.md)

## 這個專案有什麼

| 位置 | 內容 |
|---|---|
| `AGENTS.md` | 專案規則：結構、格式、流程、檢查、風格 |
| `raw/` | 7 張來源卡（書目資料與閱讀筆記，不含原文） |
| `wiki/` | LLM Wiki 本體：15 個概念頁、7 個來源頁、目錄 `index.md`、時間軸 `log.md`、討論紀錄 |
| `slides/ai-agents-101/deck.md` | 教學簡報原始檔（20 張） |
| `tools/` | `build.py`（產生網站）、`check.py`（三段檢查） |
| `checks/` | `check-log.md`（每次檢查的原始紀錄）、`run-01-journal.md`（過程與反思） |
| `docs/` | 產出的網站，GitHub Pages 讀這個資料夾 |

## 流程

```
① 蒐集 → ② 討論 → ③ 寫入 Wiki → ④ Wiki 檢查 →（每篇來源重複）
→ ⑤ 簡報大綱 → ⑥ 大綱檢查 → ⑦ 建置 → ⑧ 產出檢查 → ⑨ 交付
```

檢查失敗就退回前面的節點。完整說明在 `AGENTS.md` 第 4 節，圖在網站的「製作流程」頁。

## 自己跑一次

```bash
pip install -r requirements.txt
python tools/check.py wiki
python tools/check.py deck
python tools/build.py
python tools/check.py site
```

用瀏覽器打開 `docs/index.html` 就能看。

## 想加新內容

把這個 repo 交給任何會讀 `AGENTS.md` 的 AI 編程助手，然後說：

- 「幫我把這篇文章加進 Wiki：<網址>」
- 「用 Wiki 做一份講 MCP 的十分鐘簡報」
- 「檢查一下 Wiki」

它會照 `AGENTS.md` 的流程做，並在交付前跑完檢查。

## 來源

ReAct 論文（Yao 等，2022）、Lilian Weng〈LLM Powered Autonomous Agents〉（2023）、Anthropic〈Building effective agents〉（2024）、OpenAI〈A practical guide to building agents〉（2025）、Model Context Protocol 官方文件、AGENTS.md 官方網站、Andrej Karpathy〈LLM Wiki〉（2026）。各篇的連結與摘要見 `wiki/sources/`。

## 說明

本專案的 Wiki 內容、簡報、程式與網站皆由 AI（Claude）依 `AGENTS.md` 產生，主題、對象與方向由作者決定。內容為來源的改寫整理；若與原始來源不符，以原始來源為準。
