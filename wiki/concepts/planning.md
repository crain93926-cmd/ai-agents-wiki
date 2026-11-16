---
title: 規劃：拆解與反思
type: concept
group: 運作方式
summary: Agent 把大任務拆成小步驟，並在過程中回頭檢討、修正做法。
sources: [src-weng-agents]
updated: 2026-11-16
---

要完成「幫我規劃三天的旅行」這種任務，不可能一步到位。規劃就是 agent 把大事切小、排順序、做錯了回頭改的能力。

## 拆解任務

第一件事是把大任務拆成比較小、做得動的子目標。最簡單的做法是要求模型「一步一步想」（Chain of Thought）；進一步的做法是每一步都多想幾種可能，形成樹狀的選項再挑選（Tree of Thoughts）。[[src-weng-agents]]

## 反思與修正

第二件事是回頭看做過的行動，找出錯在哪裡，並改進後面的步驟。現實任務很難一次做對，所以這種「嘗試、檢討、再試」的能力很重要。[[react]] 屬於這一類；另一個例子是 Reflexion：讓 agent 在失敗後寫下反省，下次嘗試時拿出來參考。[[src-weng-agents]]

## 相關頁面

- [[react]]：邊想邊做的具體做法
- [[memory]]：反思的內容要靠記憶保存
- [[challenges]]：長程規劃目前仍然困難
