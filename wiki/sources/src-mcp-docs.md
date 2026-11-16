---
title: "Model Context Protocol 官方文件"
type: source
summary: MCP 官方網站的介紹頁與架構總覽，說明它是什麼、有哪些角色與元素。
short: MCP 文件
author: Model Context Protocol 專案
published: 持續更新（讀取時協定版本 2026-07-28）
url: https://modelcontextprotocol.io/docs/learn
fetched: 2026-11-16
raw: raw/2026-mcp-docs.md
updated: 2026-11-16
---

## 這篇在講什麼

官方文件的兩頁：介紹頁說明 MCP 是什麼、能做什麼；架構總覽說明參與的角色、分層，以及 server 能提供的基本元素。

## 重點

- MCP 是把 AI 應用程式接到外部系統的開放標準，文件用 USB-C 作比喻。見 [[mcp]]。
- 三個角色：host（AI 應用程式）、client（host 裡負責連線的元件）、server（提供內容的程式）。
- Server 提供 tools、resources、prompts 三種基本元素。工具的概念見 [[tools]]。
- Client 先查詢 server 有哪些工具，再呼叫；server 可以在本機或遠端。
- MCP 只規定交換內容的方式，不規定 AI 應用怎麼使用模型。

## 這篇資料的限制

- 文件隨協定版本更新，本站讀的是 2026-07-28 版；舊文章的描述可能已經不同。
- 這兩頁沒有說明 MCP 由誰在何時提出，所以本站不寫由來。
- 官方文件，重點在規格，沒有討論缺點或替代方案。

## 相關頁面

- [[mcp]]：給初學者的說明
- [[tools]]：MCP 要解決的是工具怎麼接上來
