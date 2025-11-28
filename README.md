# **Polymarket liquidity rewards bot**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Node.js](https://img.shields.io/badge/Node.js-required-6da55f.svg)
![Status](https://img.shields.io/badge/Status-production--ready-brightgreen.svg)
![Polymarket](https://img.shields.io/badge/Platform-Polymarket-blue.svg)
![Automation](https://img.shields.io/badge/Type-Market%20Maker-orange.svg)

Automated market-making system for **Polymarket** prediction markets.
Provides continuous two-sided liquidity, dynamic spread control, and full external configuration through Google Sheets.

---

## **Features**

* Real-time orderbook processing over WebSockets
* Continuous two-sided market making
* Dynamic spreads and volatility-aware price adjustments
* Google Sheets–based remote configuration
* Position size controls and risk management
* Automatic merging of fragmented positions
* Background market database updater
* Modular architecture for strategy extensions

---

## **Architecture Overview**

```
                     Google Sheets
        ┌─────────────────────────────────────┐
        │ Selected Markets • Hyperparameters  │
        └──────────────┬──────────────────────┘
                       │
                       ▼
              Configuration Layer
                       │
                       ▼
   ┌───────────────────────────────────────────────────────┐
   │                      Poly-Maker                       │
   │                                                       │
   │  WebSocket Stream  →  Orderbook Processor             │
   │                                                       │
   │  Risk & Exposure    →  Market Maker Engine            │
   │                                                       │
   │  REST Execution     →  Order Synchronization          │
   │                                                       │
   │  Node.js Merger     →  Position Consolidation         │
   └───────────────────────────────────────────────────────┘
                       │
                       ▼
                 Local Data Store
```

---

## **Repo Structure**

```
poly-maker/
 ├── poly_data/        # Core market-making logic
 ├── poly_merger/      # Node.js tool for position consolidation
 ├── poly_stats/       # Account statistics & PnL tracking
 ├── poly_utils/       # Shared helpers / utilities
 ├── data_updater/     # Background market crawler
 │
 ├── main.py           # Market maker entrypoint
 ├── update_markets.py # Market DB updater
 ├── update_stats.py   # Stats updater
 │
 ├── .env.example
 └── README.md
```

---

## **Requirements**

* Python **3.9.10+**
* Node.js
* Polymarket account
* UV package manager

---
## **Installation**

1. **Download the stable build** from the [Releases](../../releases).
2. **Extract Files**: Unzip the archive.
3. **Run**: Launch `Polyliquid.exe`

---

## **Environment Variables**

| Variable          | Description                                          |
| ----------------- | ---------------------------------------------------- |
| `PK`              | Private key used for signing Polymarket transactions |
| `BROWSER_ADDRESS` | Wallet address                                       |
| `SPREADSHEET_URL` | Google Sheet containing config                       |
| `DATA_PATH`       | Local path for market data storage                   |
| `LOG_LEVEL`       | Logging level                                        |

---

## **Google Sheets Setup**

Sheets used:

* **Selected Markets** — markets to trade
* **All Markets** — full market list
* **Hyperparameters** — spreads, liquidity, sizing

> Set `SPREADSHEET_URL` in `.env`

---

## **Commands Overview**

| File                | Purpose                         |
| ------------------- | ------------------------------- |
| `main.py`           | Main market-making engine       |
| `update_markets.py` | Fetch & update all market data  |
| `update_stats.py`   | Update stats & performance logs |

---

## **Advanced Module: Poly Merger**

Automatic position consolidation to reduce gas usage and simplify accounting.
Powered by Node.js, integrated seamlessly into the main engine.

```
poly_merger/
 ├── index.js
 ├── package.json
 └── merger.js
```

---

## **Deployment Notes**

* `data_updater` should run continuously (separate IP recommended)
* Test with minimal balances before scaling
* Log files are written based on environment configuration
* Ensure permissions are valid (wallet must have 1 UI trade)

---

## **Troubleshooting**

### **No orders appear**

* Invalid PK
* Market not selected in Google Sheet
* Insufficient balance

### **Sheets not loading**

* Wrong sheet URL
* Missing or invalid Google credentials

### **Markets not updating**

* `update_markets.py` not running
* Missing network access

---

## **License**

MIT

---
