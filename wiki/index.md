# Wiki 目錄

## 概念

- [[what-is-an-agent]]：一個以語言模型為大腦，能自己規劃、使用工具、記住事情來完成任務的系統。
- [[augmented-llm]]：在語言模型外面加上檢索、工具與記憶，就是所有 agent 系統的最小單位。
- [[agent-loop]]：Agent 不是一次回答完，而是重複「想 → 做 → 看結果」直到完成。
- [[react]]：讓模型把「想法」和「行動」交錯寫出來的做法，是 agent 循環的原型。
- [[planning]]：Agent 把大任務拆成小步驟，並在過程中回頭檢討、修正做法。
- [[memory]]：短期記憶是模型當下看得到的內容；長期記憶存在外部，需要時再查回來。
- [[tools]]：工具是 agent 能呼叫的外部功能，用來查資料、執行程式或操作其他系統。
- [[workflows-vs-agents]]：Workflow 的步驟由人事先寫好；agent 的步驟由模型自己邊做邊決定。
- [[workflow-patterns]]：串接、分流、平行、指揮分工、評分修正：五種把 LLM 呼叫組起來的固定流程。
- [[multi-agent]]：任務太複雜時可以拆給多個 agent：由一位主管指揮，或彼此交接。
- [[mcp]]：一套開放標準，讓各種 AI 應用用同一種方式接上外部的資料與工具。
- [[agents-md]]：放在專案裡的一份 Markdown，告訴 AI 這個專案的規則、結構與做事方式。
- [[llm-wiki]]：人挑資料、AI 把資料整理成互相連結的 Markdown 頁面，並持續更新。
- [[guardrails]]：用多層檢查限制 agent 能做的事，並在高風險或一直失敗時交給真人。
- [[challenges]]：上下文有限、長程規劃容易走偏、輸出不一定照格式，是 agent 常見的三個難題。

## 來源

- [[src-react]]：提出 ReAct 做法的論文（2022）。
- [[src-weng-agents]]：把 agent 整理成「LLM 大腦＋規劃、記憶、工具」的總覽文章（2023）。
- [[src-anthropic-agents]]：區分 workflow 與 agent，並整理五種常見模式的實務文章（2024）。
- [[src-openai-guide]]：給產品團隊的 agent 實務指南（2025）。
- [[src-mcp-docs]]：MCP 官方網站的介紹頁與架構總覽（2026-07-28 版）。
- [[src-agents-md]]：AGENTS.md 格式的官方網站。
- [[src-llm-wiki]]：提出 LLM Wiki 模式的想法文件（2026）。

## 關於本站

- [[workflow]]：從挑資料到產生簡報的九個節點，以及哪裡會重複、哪裡會被退回。
- [[final-project]]：期末專案構想 WikiDeck：輸入一個主題，自動建立 LLM Wiki 並產出教學簡報。

## 討論紀錄

- [[discuss-react]]：讀入 ReAct 論文之前的重點提案。
- [[discuss-weng-agents]]：讀入 Lilian Weng 文章之前的重點提案。
- [[discuss-anthropic-agents]]：讀入 Anthropic 文章之前的重點提案。
- [[discuss-openai-guide]]：讀入 OpenAI 指南之前的重點提案。
- [[discuss-mcp-docs]]：讀入 MCP 官方文件之前的重點提案。
- [[discuss-agents-md]]：讀入 AGENTS.md 官方網站之前的重點提案。
- [[discuss-llm-wiki]]：讀入 LLM Wiki gist 之前的重點提案。
