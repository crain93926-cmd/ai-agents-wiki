---
title: 討論：Karpathy〈LLM Wiki〉
type: discussion
summary: 讀入 Karpathy 的 LLM Wiki gist 之前的重點提案
updated: 2026-11-16
---

## 這篇的重點

1. 知識編譯一次、持續更新，而不是每次提問重新檢索。
2. 三層：raw（不可變）、wiki（LLM 維護）、schema（規則檔）。
3. 三種操作：ingest、query、lint。
4. index.md 是目錄，log.md 是時間軸。
5. Ingest 時先和人討論重點再寫。

## 預計新增的頁面

- [[src-llm-wiki]]：來源頁
- [[llm-wiki]]：LLM Wiki 是什麼。這一頁同時說明本站的做法
- [[workflow]]：本站的製作流程（關於本站的頁面，不是概念頁）

## 預計更新的頁面

- [[agents-md]]：補上「規則檔在 LLM Wiki 裡扮演 schema 的角色」
- [[mcp]]：相關頁面加上 [[agents-md]]
- [[workflow-patterns]]：補回「和本站的關係」一段（第三篇時因為 [[workflow]] 還不存在而被檢查擋下）

## 和既有內容的關係

- 這篇不是在講 agent 的原理，而是 agent 的一種應用：讓 coding agent 維護知識庫。放在「生態與工具」分組。
- 本站和 gist 的差異要寫清楚：本站的 raw 只放來源卡，不放原文全文。

## 想問人的問題

- 這一頁要不要放進學習路徑？提案：不放。它對理解 agent 不是必要的，放在「依主題瀏覽」與「這個網站怎麼做出來的」就好。

## 決定

- 2026-11-16：沿用授權範圍，由 AI 提案後直接採用。不放進學習路徑。
