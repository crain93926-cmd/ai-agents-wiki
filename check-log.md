# 檢查紀錄

由 `tools/check.py` 自動附加，請勿手動修改既有紀錄。

## [2026-11-16 02:12:21] wiki | FAIL（3 項） | ingest 1: src-react

- 備註：頁面數： 1、concept 2、discussion 1
- ✗ [W2] agent-loop: sources 中的 src-react 不是存在的來源頁
- ✗ [W2] react: sources 中的 src-react 不是存在的來源頁
- ✗ [W0] src-react: frontmatter 無法解析（mapping values are not allowed here）。值裡有半形冒號時要用引號包起來

## [2026-11-16 02:12:27] wiki | PASS | ingest 1: src-react（修正後）

- 備註：頁面數：concept 2、discussion 1、source 1
- ✓ 所有規則通過

## [2026-11-16 02:13:30] wiki | PASS | ingest 2: src-weng-agents

- 備註：頁面數：concept 7、discussion 2、source 2
- ✓ 所有規則通過

## [2026-11-16 02:14:47] wiki | FAIL（2 項） | ingest 3: src-anthropic-agents

- 備註：頁面數：concept 10、discussion 3、source 3
- ✗ [W3] workflow-patterns: 連到不存在的頁面 [[workflow]]
- ✗ [W3] workflow-patterns: 連到不存在的頁面 [[workflow]]

## [2026-11-16 02:14:58] wiki | PASS | ingest 3: src-anthropic-agents（修正後）

- 備註：頁面數：concept 10、discussion 3、source 3
- ✓ 所有規則通過

## [2026-11-16 02:16:03] wiki | PASS | ingest 4: src-openai-guide

- 備註：頁面數：concept 12、discussion 4、source 4
- ✓ 所有規則通過

## [2026-11-16 02:17:02] wiki | PASS | ingest 5: src-mcp-docs

- 備註：頁面數：concept 13、discussion 5、source 5
- ✓ 所有規則通過

## [2026-11-16 02:17:37] wiki | PASS | ingest 6: src-agents-md

- 備註：頁面數：concept 14、discussion 6、source 6
- ✓ 所有規則通過

## [2026-11-16 02:18:39] wiki | PASS | ingest 7: src-llm-wiki

- 備註：頁面數：concept 15、discussion 7、meta 1、source 7
- ✓ 所有規則通過

## [2026-11-16 02:18:53] site | FAIL（33 項） | 第一次建置（尚未有簡報與圖）

- 備註：檢查了 33 個 HTML、724 個站內連結
- ✗ [S1] index.html: 壞掉的連結 slides/ai-agents-101/index.html
- ✗ [S1] wiki/agent-loop.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/agents-md.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/augmented-llm.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/catalog.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/challenges.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-agents-md.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-anthropic-agents.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-llm-wiki.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-mcp-docs.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-openai-guide.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-react.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/discuss-weng-agents.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/guardrails.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/llm-wiki.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/log.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/mcp.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/memory.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/multi-agent.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/planning.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/react.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-agents-md.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-anthropic-agents.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-llm-wiki.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-mcp-docs.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-openai-guide.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-react.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/src-weng-agents.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/tools.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/what-is-an-agent.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/workflow-patterns.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/workflow.html: 壞掉的連結 ../slides/ai-agents-101/index.html
- ✗ [S1] wiki/workflows-vs-agents.html: 壞掉的連結 ../slides/ai-agents-101/index.html

## [2026-11-16 02:20:40] wiki | PASS | 加入 W9（圖檔存在）後重跑

- 備註：頁面數：concept 15、discussion 7、meta 1、source 7
- ✓ 所有規則通過

## [2026-11-16 02:20:41] site | FAIL（1 項） | 圖已補上；簡報尚未製作

- 備註：檢查了 33 個 HTML、724 個站內連結
- ✗ [S1] 33 個頁面連到不存在的 slides/ai-agents-101/index.html（index.html、wiki/agent-loop.html、wiki/agents-md.html…）

## [2026-11-16 02:21:56] deck | PASS | 簡報大綱第 1 版

- 備註：ai-agents-101：20 張投影片，引用 22 個 wiki 頁
- ✓ 所有規則通過

## [2026-11-16 02:22:07] site | PASS | 簡報第 1 版建置後

- 備註：檢查了 34 個 HTML、827 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

## [2026-11-16 02:23:32] site | PASS | 修正箭頭、頁尾、提示位置後

- 備註：檢查了 34 個 HTML、822 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

## [2026-11-16 02:25:24] wiki | PASS | 新增 final-project 頁

- 備註：頁面數：concept 15、discussion 7、meta 2、source 7
- ✓ 所有規則通過

## [2026-11-16 02:25:25] site | PASS | 新增 final-project 頁後

- 備註：檢查了 35 個 HTML、841 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

## [2026-11-16 02:27:18] wiki | PASS | 交付前最後一次全檢

- 備註：頁面數：concept 15、discussion 7、meta 2、source 7
- ✓ 所有規則通過

## [2026-11-16 02:27:18] deck | PASS | 交付前最後一次全檢

- 備註：ai-agents-101：20 張投影片，引用 22 個 wiki 頁
- ✓ 所有規則通過

## [2026-11-16 02:27:18] site | PASS | 交付前最後一次全檢

- 備註：檢查了 35 個 HTML、841 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

## [2026-11-16 02:27:19] site | PASS | 最終建置

- 備註：檢查了 35 個 HTML、842 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

## [2026-11-16 02:28:03] site | PASS | 側欄簡報出處合併顯示後

- 備註：檢查了 35 個 HTML、864 個站內連結
- 備註：S2 ai-agents-101：以 1280×720 量測 20 張，超出版面 0 張
- ✓ 所有規則通過

