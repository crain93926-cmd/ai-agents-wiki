---
title: AI agent 是什麼
type: concept
group: 基礎
summary: 一個以語言模型為大腦，能自己規劃、使用工具、記住事情來完成任務的系統。
sources: [src-weng-agents, src-anthropic-agents, src-openai-guide]
updated: 2026-11-16
---

AI agent（代理）可以想成一位「會自己想辦法把事情做完的助理」。你交代目標，它自己決定步驟、去查資料、用工具，而不是只回你一段話。

## 大腦加三個零件

一個常見的說法是：把大型語言模型（LLM）當成 agent 的大腦，再配上三個零件。**規劃**讓它把大任務拆成小步驟並檢討修正，記憶讓它記得做過什麼、需要時查得到舊資料，工具讓它能取得模型本身沒有的資訊或能力。[[src-weng-agents]]

{{diagram:agent-parts}}

## 另一種說法：代替你獨立完成任務

OpenAI 的指南把 agent 定義為**能代替使用者獨立完成任務的系統**。它用 LLM 來管理流程：判斷任務什麼時候完成、必要時修正自己的行動、做不下去時把控制權交還給人；同時依照當下的狀況挑選工具來取得資訊與採取行動。這份指南列的三個核心元件是模型、工具、指示。[[src-openai-guide]]

## 「agent」這個詞有寬有窄

不同的人講 agent，指的範圍不一樣。有人指能長時間獨立運作的系統，也有人把照固定步驟執行的系統也叫 agent。Anthropic 的做法是把兩者統稱為 agentic systems，再區分成 workflow（步驟事先寫好）與 agent（模型自己決定步驟）。本站採用這個區分，細節見 [[workflows-vs-agents]]。[[src-anthropic-agents]]

要注意用詞：OpenAI 的指南把 agent 要完成的任務流程本身也稱為 workflow，和上面「固定流程」的意思不同。讀不同來源時要先看它怎麼定義。[[src-openai-guide]]

## 相關頁面

- [[planning]]、[[memory]]、[[tools]]：三個零件各自的說明
- [[agent-loop]]：這些零件怎麼一輪一輪地運作
- [[augmented-llm]]：最小的積木
- [[workflows-vs-agents]]：agent 和固定流程的差別
- [[challenges]]：目前做不好的地方
