---
title: MCP：工具的共通插頭
type: concept
group: 生態與工具
summary: 一套開放標準，讓各種 AI 應用用同一種方式接上外部的資料與工具。
sources: [src-mcp-docs, src-anthropic-agents]
updated: 2026-11-16
---

以前每種裝置的充電線都不一樣，後來有了 USB-C，一條線可以接很多東西。MCP（Model Context Protocol）想為 AI 應用做同樣的事。

## 它解決什麼問題

Agent 要好用，就得接上各種[[tools|工具]]與資料。如果每個 AI 應用都要為每個工具各寫一套串接方式，工作量會很大。MCP 是一套**開放標準**，規定 AI 應用程式和外部系統之間怎麼交換內容，目標是「做一次，到處可接」。官方文件自己用的比喻就是 USB-C。[[src-mcp-docs]] Anthropic 談到 agent 的基本積木時，也把 MCP 列為替模型接上第三方工具的一種方式。[[src-anthropic-agents]]

## 三個角色

{{diagram:mcp}}

- **Host**：AI 應用程式本身，例如聊天助手或程式編輯器。
- Client：host 裡面負責和某一個 server 保持連線的元件。Host 會為每個 server 各建立一個 client。
- Server：提供內容的程式。可以在你的電腦上執行，也可以在遠端執行。

以上出自 [[src-mcp-docs]]。

## Server 能提供的三種東西

- Tools：AI 可以呼叫來執行動作的函式，例如查詢資料庫。
- Resources：提供背景資訊的資料，例如檔案內容。
- Prompts：可以重複使用的提示範本。

AI 應用會先問 server「你有哪些工具」，把清單交給語言模型；模型決定要用某個工具時，應用程式再把呼叫轉給對應的 server，並把結果放回對話裡。[[src-mcp-docs]]

## 它不管什麼

MCP 只規定內容怎麼交換，不規定 AI 應用要怎麼使用語言模型，也不規定拿到內容之後怎麼處理。文件會隨版本更新，本頁根據的是 2026-07-28 版。[[src-mcp-docs]]

## 相關頁面

- [[tools]]：工具本身的概念
- [[augmented-llm]]：MCP 是替基本積木接上工具的方式之一
- [[agents-md]]：另一個開放標準，管的是專案規則
