---
title: 討論：OpenAI〈A practical guide to building agents〉
type: discussion
summary: 讀入 OpenAI 2025 年 agent 實務指南之前的重點提案
updated: 2026-11-16
---

## 這篇的重點

1. 定義：agent 是「代替使用者獨立完成任務」的系統，由 LLM 管理流程。
2. 適合做 agent 的三類流程：複雜判斷、規則難維護、非結構化資料。
3. 三個核心元件：模型、工具、指示。
4. 工具分三種：資料、行動、協調。
5. 多 agent 兩種模式：manager、handoff；但建議先把單一 agent 用到極限。
6. 護欄要多層；失敗太多次或高風險動作要交給真人。

## 預計新增的頁面

- [[src-openai-guide]]：來源頁
- [[multi-agent]]：多個 agent 怎麼合作
- [[guardrails]]：護欄與人類把關

## 預計更新的頁面

- [[what-is-an-agent]]：加上 OpenAI 的定義，和前兩篇並列
- [[tools]]：加上三種工具的分類
- [[agent-loop]]：加上四種離開條件
- [[workflows-vs-agents]]：加上「哪三類流程適合 agent」

## 和既有內容的關係

- 用詞差異：[[src-anthropic-agents]] 嚴格區分 workflow 與 agent；這篇把 agent 要處理的任務本身稱為 workflow。這不是事實上的矛盾，但初學者容易混淆，要在 [[what-is-an-agent]] 說明。
- 一致：兩篇都建議從簡單開始、需要時才增加複雜度。
- 零件的說法有三種了：Weng 的「規劃、記憶、工具」、Anthropic 的「檢索、工具、記憶」、這篇的「模型、工具、指示」。三種都保留。

## 想問人的問題

- 護欄列了七種，入門簡報要講幾種？提案：Wiki 列全部，簡報只講「多層」的觀念和人類把關的兩個時機。

## 決定

- 2026-11-16：沿用授權範圍，由 AI 提案後直接採用。用詞差異在定義頁明確說明。
