---
title: "OpenAI：打造 agent 的實務指南（A practical guide to building agents）"
type: source
summary: 給產品團隊的指南：何時該做 agent、三個元件、多 agent 模式與護欄。
short: OpenAI 2025
author: OpenAI
published: 2025（PDF 未標示確切日期）
url: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
fetched: 2026-11-16
raw: raw/2025-openai-practical-guide.md
updated: 2026-11-16
---

## 這篇在講什麼

OpenAI 根據客戶部署的經驗，寫給第一次要做 agent 的產品與工程團隊的指南。從「什麼是 agent」一路講到護欄與人類介入。

## 重點

- 定義：agent 是能代替使用者獨立完成任務的系統，由 LLM 管理流程並使用工具。見 [[what-is-an-agent]]。
- 適合 agent 的三類流程：需要複雜判斷、規則難以維護、依賴非結構化資料。見 [[workflows-vs-agents]]。
- 三個核心元件是模型、工具、指示；工具分資料、行動、協調三種。見 [[tools]]。
- 單一 agent 的執行迴圈有四種離開條件。見 [[agent-loop]]。
- 多 agent 有 manager 與 decentralized handoff 兩種模式，但建議先把單一 agent 用到極限。見 [[multi-agent]]。
- 護欄要多層搭配，並在失敗過多或高風險動作時交給真人。見 [[guardrails]]。

## 這篇資料的限制

- 廠商指南，範例以 OpenAI 自家的 SDK 為主。
- PDF 沒有標示確切的發表日期，本站只記為 2025 年。

## 相關頁面

- [[guardrails]]、[[multi-agent]]：這篇獨有的兩個主題
- [[src-anthropic-agents]]：另一家公司的實務文章，可以對照著讀
