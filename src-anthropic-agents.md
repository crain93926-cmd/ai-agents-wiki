---
title: "Anthropic：打造有效的 agent（Building effective agents）"
type: source
summary: 區分 workflow 與 agent，並整理五種常見模式的實務文章。
short: Anthropic 2024
author: Anthropic 工程團隊
published: 2024-12-19
url: https://www.anthropic.com/engineering/building-effective-agents
fetched: 2026-11-16
raw: raw/2024-anthropic-building-effective-agents.md
updated: 2026-11-16
---

## 這篇在講什麼

Anthropic 整理了和許多團隊一起打造 agent 的經驗。核心訊息是：成功的做法多半很簡單，而且不是每個問題都需要 agent。

## 重點

- 把系統分成 workflow（照寫好的路徑走）與 agent（模型自己決定路徑）。見 [[workflows-vs-agents]]、[[what-is-an-agent]]。
- 基本積木是加上檢索、工具、記憶的 LLM。見 [[augmented-llm]]。
- 五種 workflow 模式：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。見 [[workflow-patterns]]。
- Agent 是在迴圈中根據環境回饋使用工具的 LLM，需要真實結果、檢查點與停止條件。見 [[agent-loop]]。
- 三個原則：保持簡單、過程透明、用心設計工具介面。工具設計見 [[tools]]。
- 自主性的代價是成本與錯誤累積。見 [[challenges]]。

## 這篇資料的限制

- 頁面上註明文中提到的許多工具後來已經改變。
- 以經驗整理為主，沒有量化的比較數字。
- workflow 與 agent 的定義是這篇自己的用法。

## 相關頁面

- [[workflows-vs-agents]]：這篇最核心的區分
- [[workflow-patterns]]：五種模式
- [[augmented-llm]]：基本積木
