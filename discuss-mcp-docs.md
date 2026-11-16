---
title: 討論：Model Context Protocol 官方文件
type: discussion
summary: 讀入 MCP 官方文件（介紹頁與架構總覽）之前的重點提案
updated: 2026-11-16
---

## 這篇的重點

1. MCP 是把 AI 應用接到外部系統的開放標準，比喻是 USB-C。
2. 三個角色：host、client、server；一個 server 配一個 client。
3. Server 提供三種東西：tools、resources、prompts。
4. 先列出有哪些工具，再呼叫；結果回到對話裡。
5. Server 可以在本機，也可以在遠端。

## 預計新增的頁面

- [[src-mcp-docs]]：來源頁
- [[mcp]]：MCP 是什麼

## 預計更新的頁面

- [[tools]]：加一段「工具怎麼接上來」，連到 [[mcp]]
- [[augmented-llm]]：Anthropic 文章本來就提到 MCP 是提供介面的方式之一，補上連結

## 和既有內容的關係

- 補充：前面的來源都說「工具要有清楚的介面」，這篇是那個介面的一種具體標準。
- 時效：文件已經是 2026-07-28 版，和早期文章描述的版本有差異（例如 sampling 已棄用）。Wiki 只寫現行文件的內容，並註明版本。

## 想問人的問題

- 要不要寫 MCP 的由來（誰、何時提出）？讀到的這兩頁沒有寫，所以提案：不寫，在來源頁的限制裡註明。

## 決定

- 2026-11-16：沿用授權範圍，由 AI 提案後直接採用。由來不寫，因為來源沒有說明。
