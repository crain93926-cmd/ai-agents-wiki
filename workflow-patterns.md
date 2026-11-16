---
title: 五種 workflow 模式
type: concept
group: 設計模式
summary: 串接、分流、平行、指揮分工、評分修正：五種把 LLM 呼叫組起來的固定流程。
sources: [src-anthropic-agents]
updated: 2026-11-16
---

固定流程不代表只有一種排法。以下五種模式像五種常見的工作安排方式，可以單獨用，也可以組合。

## 五種模式一覽

| 模式 | 一句話說明 | 適合什麼時候 |
|---|---|---|
| Prompt chaining（串接） | 把任務拆成依序的幾步，上一步的輸出交給下一步，中間可以加檢查 | 任務可以乾淨地拆成固定步驟 |
| Routing（分流） | 先判斷輸入屬於哪一類，再交給專門的處理方式 | 不同類型的輸入適合分開處理 |
| Parallelization（平行） | 同時跑多個 LLM 呼叫，再把結果彙整 | 想加快速度，或想要多個觀點提高把握 |
| Orchestrator-workers（指揮分工） | 一個中央 LLM 臨場拆任務、分派給其他 LLM、再整合 | 事先無法預測要拆成哪些子任務 |
| Evaluator-optimizer（評分修正） | 一個 LLM 產出，另一個評分並給回饋，反覆修改 | 評估標準清楚，而且反覆修改確實有幫助 |

整理自 [[src-anthropic-agents]]。

## 幾個例子

串接的例子是先寫大綱、檢查大綱、再寫全文。分流的例子是簡單問題交給小模型、困難問題交給大模型。平行有兩種變化：把任務切成互不相干的部分同時做（sectioning），或是同一件事做好幾次再比較（voting）。[[src-anthropic-agents]]

## 和本站的關係

本站自己的製作流程用到其中兩種：整體是串接（讀來源、寫 Wiki、做簡報，每一步之間有檢查），檢查不過就退回重寫的部分是評分修正。模式的定義見 [[src-anthropic-agents]]；流程本身見 [[workflow]]。

## 相關頁面

- [[workflows-vs-agents]]：為什麼這些算 workflow 而不算 agent
- [[workflow]]：本站的製作流程
