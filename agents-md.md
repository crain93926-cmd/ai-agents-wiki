---
title: AGENTS.md：給 agent 的專案說明書
type: concept
group: 生態與工具
summary: 放在專案裡的一份 Markdown，告訴 AI 這個專案的規則、結構與做事方式。
sources: [src-agents-md, src-openai-guide, src-llm-wiki]
updated: 2026-11-16
---

新同事第一天上班，通常會拿到一份「這裡的做事方式」。AGENTS.md 就是寫給 AI agent 的那一份。

## 它是什麼

AGENTS.md 是一種開放的格式：一份放在專案裡的**純 Markdown 檔**，沒有必填欄位，用來告訴會寫程式的 agent 這個專案的背景與規則。官方網站把它稱為給 agent 看的 README。網站在 2026-11-16 寫有超過 60,000 個開源專案使用。[[src-agents-md]]

## 和 README 的分工

README 是寫給人看的：專案介紹、怎麼開始。AGENTS.md 放的是 agent 需要、但放進 README 會顯得雜亂的細節，例如建置步驟、測試指令、命名與風格慣例。[[src-agents-md]]

## 通常寫些什麼

常見的段落有專案概觀、建置與測試指令、程式風格、測試說明、安全注意事項。大型專案可以在不同資料夾各放一份，agent 會採用離它正在編輯的檔案最近的那一份；使用者在對話中明確下的指示則優先於檔案內容。[[src-agents-md]]

## 為什麼 agent 需要它

Agent 的三個核心元件是模型、工具、指示，其中指示決定了 agent 的行為。指示寫得越具體、越貼近實際步驟，agent 越不容易做錯。[[src-openai-guide]] AGENTS.md 就是把「這個專案專用的指示」固定寫在檔案裡，不用每次重講。[[src-agents-md]]

## 不只用在寫程式

規則檔也可以用來管理知識庫。在 [[llm-wiki]] 的做法裡，這份檔案叫 schema：它規定頁面的結構、命名的慣例，以及讀入資料、回答問題、定期檢查的流程。不同工具慣用的檔名不同，例如 Claude Code 讀 CLAUDE.md，Codex 讀 AGENTS.md。[[src-llm-wiki]]

## 相關頁面

- [[what-is-an-agent]]：指示是 agent 的核心元件之一
- [[mcp]]：另一個讓 agent 更好用的開放標準
- [[llm-wiki]]：規則檔在知識庫裡的用法
