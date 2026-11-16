---
title: ReAct：邊想邊做
type: concept
group: 運作方式
summary: 讓模型把「想法」和「行動」交錯寫出來的做法，是 agent 循環的原型。
sources: [src-react, src-weng-agents]
updated: 2026-11-16
---

ReAct 是 Reasoning（推理）加 Acting（行動）的縮寫。它像是要求一個人「做事的時候把心裡的話說出來」：先說打算做什麼，做了之後看結果，再說下一步。

## 做法：想法、行動、觀察

模型的輸出被安排成三種內容輪流出現：**想法**（Thought，現在的判斷與打算）、行動（Action，呼叫某個工具或對環境做一件事）、觀察（Observation，行動帶回來的結果）。這三步重複很多輪，直到任務完成。[[src-react]]

## 為什麼要把想和做放在一起

只會想的模型拿不到新資訊，想錯了也沒有東西可以糾正它。只會做的模型沒有計畫，遇到意外不知道怎麼調整。ReAct 讓行動帶回外部資訊，讓推理根據新資訊修改計畫，兩邊互相補足。[[src-react]]

## 實驗結果

在兩個需要連續做決定的測試（ALFWorld、WebShop）中，ReAct 的絕對成功率比先前的模仿學習與強化學習方法分別高出 34% 與 10%，而且提示裡只放了一到兩個範例。在問答與事實查核的測試中，可以查 Wikipedia 的 ReAct 比只靠推理的做法更不容易出現幻覺。這些是 2022 年的數字。[[src-react]]

## 在整個 agent 架構裡的位置

在「大腦加三個零件」的架構中，ReAct 被歸在[[planning|規劃]]底下的「反思與修正」：模型不只執行，還能根據觀察到的結果回頭調整。[[src-weng-agents]]

## 相關頁面

- [[agent-loop]]：ReAct 的三步驟就是 agent 循環的基本形狀
- [[planning]]：ReAct 所屬的能力
