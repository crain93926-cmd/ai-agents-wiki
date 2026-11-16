---
title: "ReAct 論文（ReAct: Synergizing Reasoning and Acting in Language Models）"
type: source
summary: 提出讓語言模型交錯「推理」與「行動」的 ReAct 做法的論文。
short: ReAct 2022
author: Shunyu Yao 等七人（Princeton University、Google Research）
published: 2022-10-06（ICLR 2023）
url: https://arxiv.org/abs/2210.03629
fetched: 2026-11-16
raw: raw/2022-react-paper.md
updated: 2026-11-16
---

## 這篇在講什麼

在這篇論文之前，研究者多半把語言模型的「推理」和「行動」分開研究。作者提出 ReAct：讓模型一邊寫下想法，一邊採取行動，兩者交錯進行。

## 重點

- 流程是「想法 → 行動 → 觀察結果」，重複很多輪，直到任務完成。細節見 [[react]]。
- 行動讓模型能向外部取得新資訊；推理讓模型能擬定、追蹤並修改計畫。這就是 [[agent-loop]] 最早的清楚版本之一。
- 它是一種提示方式，不需要重新訓練模型。
- 在兩個互動式決策測試（ALFWorld、WebShop）中，絕對成功率分別比先前的方法高 34% 與 10%，而且提示中只放一到兩個範例。
- 在問答與事實查核測試中，能查資料的 ReAct 比只靠推理的方法更不容易產生幻覺。

## 這篇資料的限制

- 2022 年的研究，數字來自當時的模型與測試，不能直接代表現在的模型。
- 論文談的是提示方法，沒有討論安全性、成本或如何上線。

## 相關頁面

- [[react]]：把這篇的做法講給初學者聽
- [[agent-loop]]：ReAct 所描述的循環
