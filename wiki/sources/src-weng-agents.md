---
title: "Lilian Weng：LLM 驅動的自主 agent（LLM Powered Autonomous Agents）"
type: source
summary: 把 agent 整理成「LLM 大腦＋規劃、記憶、工具」的經典總覽文章。
short: Weng 2023
author: Lilian Weng（Lil'Log 部落格）
published: 2023-06-23
url: https://lilianweng.github.io/posts/2023-06-23-agent/
fetched: 2026-11-16
raw: raw/2023-weng-llm-agents.md
updated: 2026-11-16
---

## 這篇在講什麼

這篇文章整理了 2023 年中以前的 agent 研究，提出一個後來被廣泛引用的架構：把大型語言模型（LLM）當成大腦，再加上規劃、記憶、使用工具三個零件。

## 重點

- 架構總覽見 [[what-is-an-agent]]。
- 規劃包含拆解任務與反思修正；文中介紹了 Chain of Thought、Tree of Thoughts、LLM+P、ReAct、Reflexion、Chain of Hindsight、Algorithm Distillation 等方法。見 [[planning]]、[[react]]。
- 記憶分短期與長期；長期記憶靠向量資料庫與近似最近鄰搜尋（文中列了 LSH、ANNOY、HNSW、FAISS、ScaNN）。見 [[memory]]。
- 工具的例子包含 MRKL、TALM、Toolformer、ChatGPT Plugins、function calling、HuggingGPT、API-Bank。見 [[tools]]。
- 案例包含 ChemCrow、Generative Agents、AutoGPT、GPT-Engineer。
- 文末列出三個挑戰，見 [[challenges]]。

## 這篇資料的限制

- 2023 年的整理。文中的系統多半是當時的概念驗證。
- 偏重研究方法的介紹，沒有談產品上線時的護欄與成本。

## 相關頁面

- [[what-is-an-agent]]：這篇的架構是本站定義頁的起點
- [[planning]]、[[memory]]、[[tools]]：三個零件
- [[challenges]]：文末的三個挑戰
