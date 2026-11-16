---
title: "Model Context Protocol 官方文件：What is MCP? 與 Architecture overview"
author: Model Context Protocol 專案（modelcontextprotocol.io）
published: 持續更新的文件；讀取時的協定版本為 2026-07-28
url: https://modelcontextprotocol.io/docs/learn
fetched: 2026-11-16
kind: docs
---

讀了兩頁：介紹頁 https://modelcontextprotocol.io/docs/getting-started/intro 與架構總覽 https://modelcontextprotocol.io/docs/learn

## 閱讀筆記

- 是什麼：MCP 是把 AI 應用程式接到外部系統的開放標準。文件用 USB-C 來比喻：USB-C 讓各種裝置用同一種方式連接，MCP 讓 AI 應用程式用同一種方式連到外部系統。
- 能接什麼：資料來源（本機檔案、資料庫）、工具（搜尋引擎、計算機）、工作流程（特製的提示）。
- 文件舉的用途：讓 agent 讀你的行事曆與筆記軟體；讓程式助手依設計稿產生網頁；讓企業聊天機器人連到多個資料庫。
- 對誰有好處：開發者少寫重複的串接；AI 應用能用到一整個生態系的資料與工具；使用者得到能存取自己資料、能代為行動的 AI。
- 支援情況：文件列出 Claude、ChatGPT 等 AI 助手，以及 Visual Studio Code、Cursor 等開發工具都支援，主打「做一次，到處可接」。
- 三個角色：MCP host 是 AI 應用程式本身，負責管理一個或多個 client；MCP client 是 host 裡負責和某一個 server 保持連線、取回內容的元件；MCP server 是提供內容的程式。Host 會為每一個 server 建立一個專屬的 client。
- 本機與遠端：server 可以在本機跑（透過 stdio，通常只服務一個 client），也可以在遠端跑（透過 Streamable HTTP，通常服務很多 client）。
- 兩層：資料層定義訊息的內容與意義，以 JSON-RPC 2.0 為基礎；傳輸層負責連線、訊息怎麼送、以及授權。
- Server 能提供三種基本元素（primitives）：tools（AI 可以呼叫來執行動作的函式）、resources（提供背景資訊的資料，如檔案內容、資料庫紀錄）、prompts（可重複使用的提示範本）。
- 探索與呼叫：client 先用 `tools/list` 之類的方法查詢 server 有哪些東西，再用 `tools/call` 執行某個工具。每個工具有名稱、說明、輸入格式（JSON Schema）。
- 在 AI 應用裡的流程：應用程式把所有已連線 server 的工具彙整成一份清單交給語言模型；模型決定要用某個工具時，應用程式把呼叫轉給對應的 server，再把結果放回對話。
- 通知：server 的工具清單改變時可以通知 client，client 需要先訂閱。
- Client 這一邊也能提供功能：elicitation 讓 server 可以向使用者要求補充資訊或確認。
- 範圍：MCP 只規定交換內容的協定，不規定 AI 應用程式怎麼使用 LLM 或怎麼管理這些內容。

## 值得注意

- 文件會隨協定版本改變。讀取時的版本（2026-07-28）是無狀態的設計：每個請求都自帶協定版本與能力資訊，server 用 `server/discover` 公布自己支援什麼。
- 同一版文件註明 client 端的 sampling 與 logging 兩項功能已被標為棄用。舊文章裡關於這兩項的描述可能已經過時。
- 文件沒有在這兩頁說明 MCP 是誰在什麼時候提出的，本來源卡不記錄這一點。
