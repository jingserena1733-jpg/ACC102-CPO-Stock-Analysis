# ACC102-CPO-Stock-Analysis
ACC102 Course Project: A data-driven analysis of CPO-related firms using WRDS CRSP data. This repository integrates Python-based data processing, financial performance, risk and liquidity analysis, and an interactive Streamlit dashboard for exploring market dynamics and firm characteristics.
# CPO-Related Stocks Analysis Dashboard (3 Companies: AVGO, INTC, NVDA)

## 1. Problem & User (1-2 sentences)

**Problem:** Investors and finance students lack a simple, interactive tool to compare market performance and key trading metrics (liquidity, growth, volatility) of three major semiconductor companies involved in Co‑Packaged Optics (CPO) – a critical technology for AI data centres.

**Target User:** Retail investors, finance students, and anyone interested in AI hardware stocks (NVIDIA, Broadcom, Intel).

## 2. Data

- **Source:** WRDS (Wharton Research Data Services) – CRSP Daily Stock database.
- **Access Date:** April 2026 (data covers January 2020 – December 2024).
- **Companies:** AVGO (Broadcom), INTC (Intel), NVDA (NVIDIA).
- **Key Fields:** date, ticker, price (prc), return (ret), volume (vol), shares outstanding (shrout), bid, ask, market cap (prc * shrout), spread (ask - bid).
- **Note:** The processed CSV file (`cpo_stock_processed.csv`) is included in this repository (< 25 MB). The original WRDS query script is available on request.

## 3. Methods (Main Python Steps)

1. **Load & Clean** – Read CSV, parse dates, filter valid tickers.
2. **Sidebar Filters** – User selects tickers, date range, and chart metric.
3. **KPIs** – Average daily return, daily volatility, average volume (single or multiple companies).
4. **Financial Indicators (from actual trading data)** – Compute:
   - Latest Market Cap
   - Price Growth (%) over the selected period
   - Average Daily Volume (M shares)
   - Average Spread (USD)
   - Annualized Volatility (%)
   - Highest / Lowest Price
5. **Financial Dimension Evaluation** – Interpret liquidity, growth (price‑based), and risk based on computed metrics.
6. **Interactive Chart** – Line plot of Return, Volume, Spread, or Market Cap over time.
7. **Company Insights** – Static analysis and news links for each selected company (NVDA, AVGO, INTC).

## 4. Key Findings (3-5 bullets)

- **NVIDIA** shows the strongest price growth (>500% over the period) and highest annualized volatility (>60%), reflecting AI hype and elevated expectations.
- **Broadcom** has lower volatility (~30%) and tighter spreads, indicating a more stable, diversified business model.
- **Intel** experienced negative price growth and lower liquidity, consistent with its ongoing turnaround challenges.
- Liquidity (volume + spread) is strongly correlated with market capitalisation; large‑caps are much more efficient to trade.

## 5. How to Run

### Prerequisites
- Python 3.8 or higher
- Required packages: `streamlit`, `pandas`, `matplotlib`, `numpy`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cpo-stocks-dashboard.git
   cd cpo-stocks-dashboard
