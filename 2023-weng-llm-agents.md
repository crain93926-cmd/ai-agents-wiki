---
title: "LLM Powered Autonomous Agents"
author: Lilian Weng（Lil'Log 部落格）
published: 2023-06-23
url: https://lilianweng.github.io/posts/2023-06-23-agent/
fetched: 2026-11-16
kind: blog
---

## 閱讀筆記

- 核心架構：把 LLM 當成 agent 的「大腦」（控制中心），再配上三個零件：規劃（planning）、記憶（memory）、使用工具（tool use）。
- 規劃分兩件事：（1）把大任務拆成小的子目標；（2）反思與修正，也就是回頭檢討做過的行動、從錯誤中學習、改進後續步驟。
- 拆解任務的方法舉例：Chain of Thought（要求模型一步一步想）、Tree of Thoughts（每一步探索多種想法，形成樹狀）、LLM+P（把長程規劃交給外部的傳統規劃器）。
- 反思的方法舉例：ReAct（推理與行動交錯）、Reflexion（讓 agent 在失敗後寫下反省並存進記憶，下次嘗試時參考）、Chain of Hindsight、Algorithm Distillation。
- 記憶：作者把人的記憶類比到 agent。短期記憶對應「上下文內的學習」，受上下文視窗長度限制；長期記憶對應外部的向量資料庫，需要時用快速檢索取回。
- 長期記憶的檢索依賴近似最近鄰搜尋，文中列了 LSH、ANNOY、HNSW、FAISS、ScaNN 等演算法。
- 工具：呼叫外部 API，取得模型權重裡沒有的東西，例如最新資訊、執行程式碼的能力、專有資料來源。舉的例子有 MRKL、TALM、Toolformer、ChatGPT Plugins 與 function calling、HuggingGPT、API-Bank。
- 案例：ChemCrow（化學工具）、科學發現 agent、Generative Agents（有記憶、反思、規劃的模擬角色）、AutoGPT、GPT-Engineer。
- 文末列出三個挑戰：（1）上下文長度有限；（2）長程規劃與任務拆解困難，遇到意外錯誤時不容易調整；（3）自然語言介面不可靠，模型可能輸出格式錯誤或不照指示做，所以很多 agent 程式碼其實在處理輸出的解析。

## 值得注意

- 這是 2023 年中的整理，文中舉的系統（AutoGPT 等）是當時的概念驗證，不代表現在的做法。
- 「LLM 是大腦＋規劃、記憶、工具」是這篇的框架，不是唯一的定義。
- 作者指出向量檢索的表達能力不如完整的注意力機制，也就是說外部記憶不能完全取代上下文。
