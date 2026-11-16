---
title: "AI Agents 是什麼？"
audience: 沒有寫過程式、第一次聽到 AI agent 的大學生
goal: 能用自己的話說明 agent 是什麼、怎麼運作、什麼時候該用、要注意什麼
duration: 20
wiki_scope: [what-is-an-agent, augmented-llm, agent-loop, react, planning, memory, tools, workflows-vs-agents, workflow-patterns, mcp, agents-md, guardrails, challenges]
---

<!-- layout: title -->
## Agent 筆記本・教學簡報
# AI Agents 是什麼？

給第一次聽到這個詞的人：看懂它**怎麼運作**、**什麼時候該用**、**要小心什麼**。

---

<!-- layout: objectives | refs: what-is-an-agent, agent-loop, workflows-vs-agents, guardrails -->
## 學習目標
# 看完你會知道

1. Agent 和一般的聊天機器人差在哪裡
2. Agent 怎麼一步一步把事情做完
3. 什麼時候該用 agent，什麼時候不該
4. 讓 agent 動手之前，要先準備什麼

---

<!-- layout: bullets | refs: tools, agent-loop -->
## 從你熟悉的開始
# 只會聊天的模型，有三件事做不到

- 不知道**訓練之後**才發生的事
- 不能自己執行程式，也讀不到你的資料
- 你問一句，它答一句，答完就結束

它很會「說」，但不會「做」。

---

<!-- layout: big | refs: what-is-an-agent -->
## 一句話
# Agent 是拿到目標後，會自己想辦法把事情做完的 AI 系統

你交代目標。它自己決定步驟、查資料、用工具；做不下去時，把控制權交還給你。

---

<!-- layout: diagram | refs: what-is-an-agent, augmented-llm -->
## 組成
# 一個大腦，三個零件

{{diagram:agent-parts}}

不同來源的說法略有出入，但都離不開：模型、工具、記憶，加上清楚的指示。

---

<!-- layout: cards | refs: planning, memory, tools -->
## 三個零件
# 各自負責什麼

- **規劃** 把大任務拆成小步驟；做錯了回頭檢討、修正
- **記憶** 短期是當下看得到的內容；長期存在外部，需要時查回來
- **工具** 查資料、執行程式、操作其他系統，取得模型本身沒有的能力

---

<!-- layout: diagram | refs: agent-loop -->
## 運作方式
# 想 → 做 → 看，重複到可以停

{{diagram:agent-loop}}

---

<!-- layout: trace | refs: react, agent-loop -->
## 示意：請 agent 判斷今天要不要帶傘
# 把心裡的話寫出來：ReAct

```
想法　我需要知道今天下午會不會下雨
行動　呼叫「天氣查詢」工具（地點：台北）
觀察　下午降雨機率偏高
想法　資訊夠了，可以回答
回答　下午很可能下雨，記得帶傘
```

這是自編的示意。重點：每個「想法」都根據上一步真實的「觀察」。

---

<!-- layout: bullets | refs: agent-loop, react -->
## 循環的兩個關鍵
# 看到真實結果，並且知道何時停

- 每做一步都要拿到**真實的結果**，不能靠模型自己想像
- 停止條件事先設好：任務完成、達到回合上限、發生錯誤
- 卡住或到了檢查點，就停下來問人
- ReAct 在 2022 年的兩個決策測試中，絕對成功率比先前的方法高 34% 與 10%

---

<!-- layout: quiz | refs: what-is-an-agent, agent-loop, guardrails -->
## 小測驗 1
# 下面哪一個最像 agent？

1. 你問「台北到高雄多遠」，模型直接回答
2. 你說「幫我訂下週去高雄最便宜的車票」，系統自己查班次、比價，訂票前先問你
3. 程式每天早上固定把新聞標題寄給你

> 答案是 B。它拿到的是目標，自己決定步驟並使用工具，重要動作前會停下來問人。A 是一次問答，C 是寫死的排程。

---

<!-- layout: diagram | refs: workflows-vs-agents -->
## 不是什麼都要用 agent
# 差別在：誰決定下一步

{{diagram:workflow-vs-agent}}

---

<!-- layout: compare | refs: workflows-vs-agents, challenges -->
## 怎麼選
# 先用最簡單的做法

| 適合固定流程（workflow） | 適合 agent |
|---|---|
| 步驟明確，可以事先寫好 | 需要複雜的臨場判斷 |
| 希望結果穩定、可預測 | 規則多到難以維護 |
| 在意成本與等待時間 | 資料是文件、對話這類非結構化內容 |

Agent 是拿**更多時間與成本**去換表現。很多需求一次模型呼叫加上檢索就夠了。

---

<!-- layout: bullets | refs: workflow-patterns -->
## 固定流程也有很多種
# 五種 workflow 模式

| 模式 | 一句話 |
|---|---|
| 串接 | 拆成依序的幾步，中間可以加檢查 |
| 分流 | 先分類，再交給專門的處理方式 |
| 平行 | 同時做很多份，再彙整 |
| 指揮分工 | 一個中央模型拆任務、分派、整合 |
| 評分修正 | 一個產出，一個評分，反覆修改 |

---

<!-- layout: diagram | refs: mcp, tools -->
## 工具怎麼接上來
# MCP：AI 應用的共通插頭

{{diagram:mcp}}

---

<!-- layout: bullets | refs: agents-md, llm-wiki -->
## 讓 agent 懂你的專案
# AGENTS.md：寫給 agent 的說明書

- 一份放在專案裡的純 Markdown，沒有必填欄位
- README 給人看；AGENTS.md 放建置步驟、測試指令、命名與風格慣例
- 指示越具體，agent 越不容易做錯
- 這份簡報所在的網站，就是 AI 照著一份規則檔維護的知識庫

---

<!-- layout: cards | refs: guardrails, tools -->
## 放手之前
# 護欄與人類把關

- **多層護欄** 沒有哪一種單獨就夠：範圍檢查、安全檢查、個資過濾、工具分級
- **高風險先問人** 付款、取消訂單、大額退款，在可靠度被驗證前都先經過人
- **一直失敗就交棒** 多次無法理解使用者的意圖時，交給真人處理

---

<!-- layout: bullets | refs: challenges -->
## 目前的限制
# Agent 還做不好的事

- **上下文有限**：指示、紀錄、工具結果都擠在同一個視窗
- 步驟一多容易偏離計畫，遇到意外不容易調整
- 輸出可能不照格式，程式要花力氣檢查
- 每一步都建立在上一步之上，小錯會累積成大錯
- 比較慢，也比較貴

---

<!-- layout: quiz | refs: workflows-vs-agents, multi-agent -->
## 小測驗 2
# 公司想自動彙整「每月格式固定的報表」，你會建議？

1. 做一個完全自主的 agent，讓它自己決定怎麼做
2. 用固定流程：步驟寫好，每一步之後檢查
3. 讓多個 agent 互相交接

> 答案是 B。步驟明確、希望結果可預測時，固定流程比較合適，也比較省。需要臨場判斷時才考慮 agent；一個 agent 不夠用時才考慮多個。

---

<!-- layout: recap | refs: what-is-an-agent, agent-loop, workflows-vs-agents, mcp, agents-md, guardrails -->
## 帶走這五件事
# 重點回顧

1. Agent 以模型為大腦，加上工具、記憶與規劃，拿到目標後自己把事情做完
2. 它靠「想 → 做 → 看」的循環運作，每一步都要看到真實結果
3. 先用最簡單的做法；步驟明確就用固定流程
4. MCP 負責接工具，AGENTS.md 負責給規則
5. 動手之前先設好護欄、停止條件與人類把關

---

<!-- layout: sources | refs: src-react, src-weng-agents, src-anthropic-agents, src-openai-guide, src-mcp-docs, src-agents-md, src-llm-wiki -->
## 這份簡報根據的資料
# 來源

- [[src-react|ReAct 論文]]：Yao 等人，2022
- [[src-weng-agents|LLM Powered Autonomous Agents]]：Lilian Weng，2023
- [[src-anthropic-agents|Building effective agents]]：Anthropic，2024
- [[src-openai-guide|A practical guide to building agents]]：OpenAI，2025
- [[src-mcp-docs|Model Context Protocol 官方文件]]、[[src-agents-md|AGENTS.md 官方網站]]
- [[src-llm-wiki|LLM Wiki]]：Andrej Karpathy，2026

每張投影片左下角的標籤可以點回 Wiki；Wiki 的每一段都標了來源。
