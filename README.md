# ACC102-CPO-Stock-Analysis
ACC102 Course Project: A data-driven analysis of CPO-related firms using WRDS CRSP data. This repository integrates Python-based data processing, financial performance, risk and liquidity analysis, and an interactive Streamlit dashboard for exploring market dynamics and firm characteristics.

## 1. Problem & User

**Problem:** Investors and finance students lack a simple, interactive tool to compare market performance and key trading metrics (liquidity, growth, volatility) of three major semiconductor companies involved in Co‑Packaged Optics (CPO) – a critical technology for AI data centres.

**Target User:** Retail investors, finance students, and anyone interested in AI hardware stocks (NVIDIA, Broadcom, Intel).

## 2. Data

- **Source:** WRDS (Wharton Research Data Services) – CRSP Daily Stock database.
- **Access Date:** April 2026 (data covers January 2020 – December 2024).
- **Companies:** AVGO (Broadcom), INTC (Intel), NVDA (NVIDIA).
- **Key Fields:** date, ticker, price (prc), return (ret), volume (vol), shares outstanding (shrout), bid, ask, market cap (prc * shrout), spread (ask - bid).

## 3. Methods (Main Python Steps)

1. **Load & Clean** –Use pandas to save WRDS data as CSV after retrieving it via the WRDS Python interface, Read CSV, parse dates, filter valid tickers.
2. **Sidebar Filters** – User selects tickers, date range, and chart metric.
3. **KPIs** – Average daily return, daily volatility, average volume.
4. **Financial Indicators** – Compute Market Cap, Price Growth, Avg Volume, Avg Spread, Annualized Volatility, Highest/Lowest Price.
5. **Financial Dimension Evaluation** – Interpret liquidity, growth, and risk.
6. **Interactive Chart** – Line plot of Return, Volume, Spread, or Market Cap over time.
7. **Company Insights** – Static analysis and news links for NVDA, AVGO, INTC.

## 4. Key Findings

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
   git clone https://github.com/jingserena1733-jpg/ACC102-CPO-Stock-Analysis.git
   cd ACC102-CPO-Stock-Analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. The dashboard will open in your browser. Use the sidebar to select companies, date range, and chart metric.

### Repository structure
```
.
├── app.py                     # Main Streamlit application
├── cpo_stock_processed.csv    # Processed WRDS data (AVGO, INTC, NVDA)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 6. Product Link / Demo

- **GitHub Repository:** (https://github.com/jingserena1733-jpg/ACC102-CPO-Stock-Analysis)
- **Demo Video:** 

## 7. Limitations & Next Steps

- **Limitations:**
  - Only three companies are included (NVDA, AVGO, INTC). More CPO-related firms could be added.
  - The analysis is purely backward‑looking and does not forecast future stock movements.
- **Next Steps:**
  - Add a simple momentum indicator (e.g., moving average crossover) to support trading decisions.
  - Deploy to Streamlit Community Cloud for instant online access.


