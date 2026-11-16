---
title: "Karpathy：LLM Wiki"
type: source
summary: 提出「讓 LLM 維護一個 Markdown 知識庫」這個模式的想法文件。
short: Karpathy 2026
author: Andrej Karpathy
published: 2026-04-04
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
fetched: 2026-11-16
raw: raw/2026-karpathy-llm-wiki.md
updated: 2026-11-16
---

## 這篇在講什麼

一份描述做法的想法文件：與其每次提問都重新檢索原始文件，不如讓 LLM 把知識整理成一個持續更新的 wiki。

## 重點

- 三層結構（原始來源、wiki、schema）與三種操作（ingest、query、lint）。見 [[llm-wiki]]。
- 規則檔（CLAUDE.md 或 AGENTS.md）在這個模式裡是 schema。見 [[agents-md]]。
- index.md 當目錄、log.md 當時間軸。
- 人挑來源與提問，LLM 做整理與維護。
- 本站依這個模式製作，流程見 [[workflow]]。

## 這篇資料的限制

- 想法文件，沒有程式碼也沒有實驗數據。
- 作者說的「靠目錄就夠、不需要向量檢索」以中等規模為前提。

## 相關頁面

- [[llm-wiki]]：給初學者的說明
- [[workflow]]：本站怎麼照這個模式實作
