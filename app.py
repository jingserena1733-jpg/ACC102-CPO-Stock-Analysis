import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===================== APP TITLE =====================
st.title("CPO-Related Stocks Analysis Dashboard")

# ===================== CPO INTRODUCTION =====================
st.markdown("""
## What is CPO (Co-Packaged Optics)?

Co-Packaged Optics (CPO) is an emerging technology that integrates optical components 
directly with semiconductor chips to improve data transmission speed and energy efficiency.

It plays a critical role in:
- AI infrastructure
- Data centers
- High-speed communication networks

This dashboard analyzes the financial performance of major firms involved in this sector 
using WRDS CRSP data.
""")

# ===================== LOAD DATA =====================
df = pd.read_csv("cpo_stock_processed.csv")
df['date'] = pd.to_datetime(df['date'])

# Ensure ticker is used instead of PERMNO (for clarity)
# (Assumes your dataset already includes ticker column from WRDS join)

# ===================== SIDEBAR =====================
st.sidebar.header("User Input")

# Select multiple companies (using ticker symbols)
tickers = sorted(df['ticker'].unique())
selected_tickers = st.sidebar.multiselect(
    "Select Companies",
    tickers,
    default=tickers
)

# Select date range
start_date = st.sidebar.date_input("Start Date", df['date'].min())
end_date = st.sidebar.date_input("End Date", df['date'].max())

# Select metric
metric = st.sidebar.selectbox(
    "Select Metric",
    ["Return", "Volume", "Spread", "Market Cap"]
)

# ===================== FILTER DATA =====================
filtered_df = df[
    (df['ticker'].isin(selected_tickers)) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]

# ===================== KPI SECTION =====================
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Return",
    round(filtered_df['ret'].mean(), 5)
)

col2.metric(
    "Volatility (Std Dev)",
    round(filtered_df['ret'].std(), 5)
)

col3.metric(
    "Average Volume",
    int(filtered_df['vol'].mean())
)

# ===================== DATA PREVIEW =====================
st.subheader("Data Overview")
st.write(filtered_df.head())

# ===================== CHART =====================
st.subheader(f"{metric} Comparison Across Companies")

fig, ax = plt.subplots()

for t in selected_tickers:
    temp = filtered_df[filtered_df['ticker'] == t]

    if metric == "Return":
        ax.plot(temp['date'], temp['ret'], label=t)

    elif metric == "Volume":
        ax.plot(temp['date'], temp['vol'], label=t)

    elif metric == "Spread":
        ax.plot(temp['date'], temp['spread'], label=t)

    elif metric == "Market Cap":
        ax.plot(temp['date'], temp['market_cap'], label=t)

# Labels and legend
ax.set_xlabel("Date")
ax.set_title(f"{metric} Comparison Across Selected Companies")
ax.legend()

# Display plot
st.pyplot(fig)

# ===================== INTERPRETATION =====================
st.subheader("Interpretation")

st.write("""
- Firms such as NVIDIA and Broadcom tend to show stronger returns due to AI-driven demand.
- Higher volatility indicates greater exposure to market fluctuations and investor sentiment.
- Lower bid-ask spreads suggest better liquidity and more efficient trading.
- Market capitalization differences highlight variation in firm size and industry dominance.
""")

# ===================== FOOTER =====================
st.sidebar.markdown("---")
st.sidebar.write("Developed using WRDS and Streamlit")