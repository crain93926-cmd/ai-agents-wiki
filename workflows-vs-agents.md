---
title: Workflow 與 agent 的差別
type: concept
group: 設計模式
summary: Workflow 的步驟由人事先寫好；agent 的步驟由模型自己邊做邊決定。
sources: [src-anthropic-agents, src-openai-guide]
updated: 2026-11-16
---

想像兩種員工：一種照著標準作業流程一步一步做；另一種只拿到目標，自己決定怎麼做。兩種都用得到語言模型，但適合的任務不一樣。

## 兩種架構

Workflow（固定流程）是指 LLM 和工具**照著事先寫好的程式路徑**執行。Agent 則是由 LLM 自己動態決定流程和要用的工具，自己掌握怎麼完成任務。兩者可以統稱為 agentic systems。[[src-anthropic-agents]]

{{diagram:workflow-vs-agent}}

## 怎麼選

原則是先找最簡單的解法，真的需要才增加複雜度。任務明確、希望結果可預測時，用 workflow。需要彈性、必須靠模型臨場判斷時，才用 agent。很多應用其實只要把單次的 LLM 呼叫配上檢索與好的範例就夠了。[[src-anthropic-agents]]

## 哪些任務值得用 agent

OpenAI 的指南舉出三類傳統規則式自動化處理不好、比較適合 agent 的任務：需要複雜判斷的（例如退款核准）、規則多到難以維護的（例如供應商安全審查）、大量依賴非結構化資料的（例如處理保險理賠文件）。不屬於這三類的話，確定性的做法可能就夠了。[[src-openai-guide]]

## 代價

Agentic system 通常是拿更長的等待時間和更高的成本，去換更好的任務表現。選用之前要先確定這個交換值得。[[src-anthropic-agents]]

## 相關頁面

- [[workflow-patterns]]：五種常見的 workflow 模式
- [[agent-loop]]：agent 這一邊是怎麼運作的
- [[multi-agent]]：一個 agent 不夠時怎麼分工
- [[challenges]]：放手讓模型決定的風險
