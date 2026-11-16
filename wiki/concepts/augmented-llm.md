---
title: 基本積木：加了配備的 LLM
type: concept
group: 基礎
summary: 在語言模型外面加上檢索、工具與記憶，就是所有 agent 系統的最小單位。
sources: [src-anthropic-agents]
updated: 2026-11-16
---

單獨的語言模型像一位只能靠記憶回答的人。給他一本可以查的資料、幾樣工具和一本筆記本，他能做的事就多很多。這個「加了配備的模型」是後面所有做法的起點。

## 三樣配備

這個基本積木叫 augmented LLM（擴充過的 LLM）：一個 LLM 加上**檢索、工具、記憶**。模型可以自己產生搜尋用的查詢、挑選適合的工具、決定哪些資訊要留下來。[[src-anthropic-agents]]

## 設計時的兩個建議

第一，依照實際用途調整這些配備，不要一次全裝。第二，給模型的介面要清楚、有完整的說明文件，模型才知道每樣東西怎麼用。[[mcp]] 是提供這種介面的方式之一。[[src-anthropic-agents]]

## 相關頁面

- [[what-is-an-agent]]：另一種「大腦加三個零件」的說法
- [[tools]]、[[memory]]：配備的細節
- [[workflows-vs-agents]]：把積木組起來的兩種方式
- [[mcp]]：接上外部工具的標準
