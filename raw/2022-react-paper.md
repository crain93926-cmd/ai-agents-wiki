---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
author: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao（Princeton University、Google Research）
published: 2022-10-06（arXiv v1）；2023-03-10 v3 為 ICLR 2023 定稿版
url: https://arxiv.org/abs/2210.03629
fetched: 2026-11-16
kind: paper
---

## 閱讀筆記

- 問題意識：在這篇之前，語言模型的「推理」（例如 chain-of-thought，一步一步想）和「行動」（例如產生行動計畫）大多被分開研究。作者主張兩者應該合在一起。
- 做法：讓模型交錯產生「推理紀錄」和「針對任務的行動」。推理幫助模型擬定計畫、追蹤進度、修改計畫、處理例外；行動讓模型能向外部（知識庫或環境）取得新資訊。
- 常見的提示格式是 Thought（想法）→ Action（行動）→ Observation（觀察到的結果），重複很多輪。
- ReAct 不是新的模型架構，而是一種提示方式，用少量範例示範就能套用。
- 問答與事實查核（HotpotQA、Fever）：模型可以呼叫一個簡單的 Wikipedia API。作者指出，這樣能減輕純 chain-of-thought 推理常見的幻覺與錯誤一路傳下去的問題，而且解題過程比沒有推理紀錄的方法更容易讓人看懂。
- 互動式決策（ALFWorld、WebShop）：ReAct 的成功率比模仿學習與強化學習方法分別高出絕對值 34% 與 10%。
- 作者主張的好處：效果更好，而且人比較容易理解與信任模型的過程。

## 值得注意

- 34% 與 10% 是「絕對成功率的差距」，不是相對提升。
- 上述結果是在提示中只放一到兩個範例的條件下得到的。
- 這是 2022 年的研究，使用的是當時的模型；數字不能直接套用到現在的模型。
