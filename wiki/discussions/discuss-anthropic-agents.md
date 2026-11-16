---
title: 討論：Anthropic〈Building effective agents〉
type: discussion
summary: 讀入 Anthropic 2024 年 agent 實務文章之前的重點提案
updated: 2026-11-16
---

## 這篇的重點

1. 最重要的區分：workflow（路徑由程式寫死）與 agent（路徑由模型自己決定）。
2. 先用最簡單的做法，需要時才升級；agent 是用時間和成本換表現。
3. 基本積木是 augmented LLM（加上檢索、工具、記憶的 LLM）。
4. 五種 workflow 模式。
5. Agent 的循環每一步都要從環境拿到真實結果，並設定停止條件。
6. 工具的說明要寫得跟提示一樣用心（ACI）。

## 預計新增的頁面

- [[src-anthropic-agents]]：來源頁
- [[augmented-llm]]：基本積木
- [[workflows-vs-agents]]：兩種架構的差別與選擇
- [[workflow-patterns]]：五種模式

## 預計更新的頁面

- [[what-is-an-agent]]：補上「agentic systems」底下 workflow 與 agent 的區分
- [[agent-loop]]：補上環境回饋、檢查點、停止條件
- [[tools]]：補上工具設計的原則
- [[challenges]]：補上成本、延遲、錯誤累積

## 和既有內容的關係

- 補充：[[src-weng-agents]] 的「大腦＋三零件」和這篇的「augmented LLM（檢索、工具、記憶）」很接近，但用詞不同。兩種說法都保留，各自標來源。
- 沒有矛盾。

## 想問人的問題

- 五種模式的英文名稱要不要翻譯？提案：保留英文，後面加一句中文解釋，因為實務上大家都用英文講。

## 決定

- 2026-11-16：沿用授權範圍，由 AI 提案後直接採用。模式名稱保留英文並附中文解釋。
