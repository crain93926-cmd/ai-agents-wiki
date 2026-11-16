---
title: 多個 agent 一起工作
type: concept
group: 設計模式
summary: 任務太複雜時可以拆給多個 agent：由一位主管指揮，或彼此交接。
sources: [src-openai-guide, src-anthropic-agents]
updated: 2026-11-16
---

一個人事情太多、工具太雜的時候，就會考慮分工。Agent 也一樣。不過分工有溝通成本，所以不是越多越好。

## 先把單一 agent 用到極限

建議的順序是先用一個 agent，把它的工具與指示調到最好。只有在提示裡的條件判斷變得太複雜，或工具太多太相似、把說明寫清楚也分不出來的時候，才考慮拆成多個 agent。[[src-openai-guide]]

## 兩種分工方式

- **Manager 模式**：一個中央 agent 像主管，把各個專門的 agent 當成工具來呼叫。它自己保有和使用者對話的主導權，最後負責整合結果。
- Decentralized handoff 模式：幾個地位對等的 agent，依照專長把控制權整個交接給下一位，適合「先分流、再由專人處理」的情境。

以上兩種模式出自 [[src-openai-guide]]。

## 和 orchestrator-workers 的關係

[[workflow-patterns]] 裡的 orchestrator-workers（指揮分工）也是「一個中央 LLM 拆任務、分派、整合」，和 manager 模式的想法相近。[[src-anthropic-agents]]

## 相關頁面

- [[workflow-patterns]]：指揮分工模式
- [[tools]]：把其他 agent 當工具，屬於「協調類」工具
