---
title: "AGENTS.md（官方網站）"
author: AGENTS.md 專案（現由 Linux Foundation 旗下的 Agentic AI Foundation 維護）
published: 持續更新的網站
url: https://agents.md/
fetched: 2026-11-16
kind: spec
---

## 閱讀筆記

- 是什麼：AGENTS.md 是一種開放、單純用 Markdown 寫的檔案格式，用來給「會寫程式的 AI agent」專案層級的指引。網站稱它是給 agent 看的 README。
- 沒有必填欄位，就是一般的 Markdown，標題與內容自己決定。
- 和 README.md 的分工：README 寫給人看（快速開始、專案介紹、貢獻方式）；AGENTS.md 放 agent 需要、但會讓 README 變雜亂的細節，例如建置步驟、測試指令、專案慣例。
- 常見段落：專案概觀、建置與測試指令、程式風格、測試說明、安全注意事項；也有人加上 commit 或 pull request 的規則、部署步驟。
- 大型專案可以在子資料夾各放一份 AGENTS.md。Agent 會讀離被編輯檔案最近的那一份；使用者在對話中明確下的指示優先於一切。
- 支援的工具很多，網站列出 OpenAI Codex、Google Jules、Cursor、Aider、Gemini CLI、GitHub Copilot 的 coding agent、VS Code、Devin、Windsurf、Zed 等。
- 維護者：Agentic AI Foundation（屬於 Linux Foundation）。網站提到這個格式是多個 agent 工具的團隊共同合作的成果。
- 採用情況：網站寫有超過 60,000 個開源專案使用；並舉例 OpenAI 的主要 repo 在撰寫當時有 88 份 AGENTS.md。

## 值得注意

- 採用數字是網站自己的說法，會隨時間改變。
- 網站是推廣這個格式的一方，沒有討論缺點。
- 不是每個工具都用這個檔名；有些工具有自己的規則檔（例如 Claude Code 用 CLAUDE.md）。這一點來自另一篇來源（LLM Wiki gist），不是這個網站說的。
