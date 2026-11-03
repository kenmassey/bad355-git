# thanks Gemini!

import streamlit as st
import duckdb
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="U.S. Treasury Yield Dashboard", layout="wide")
st.title("📈 U.S. Treasury Yield Curve Dashboard")

# explain what this does
@st.cache_data(ttl=3600)
def load_data():
    conn = duckdb.connect()
    hf_url = "hf://datasets/defeatbeta/yahoo-finance-data/data/US/daily_treasury_yield.parquet"
    
    query = f"""
        SELECT 
            TRY_CAST(report_date AS DATE) AS date,
            bc_1month AS "1 Mo",
            bc_3month AS "3 Mo",
            bc_6month AS "6 Mo",
            bc_1year  AS "1 Yr",
            bc_2year  AS "2 Yr",
            bc_5year  AS "5 Yr",
            bc_10year AS "10 Yr",
            bc_30year AS "30 Yr"
        FROM '{hf_url}'
        WHERE report_date IS NOT NULL
        ORDER BY date ASC
    """
    df = conn.sql(query).df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Options")

min_date = df["date"].min()
max_date = df["date"].max()

# Date range slider
start_date, end_date = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD"
)

# Filter DataFrame by selected date range
filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

# --- Maturity Selector ---
all_maturities = ["1 Mo", "3 Mo", "6 Mo", "1 Yr", "2 Yr", "5 Yr", "10 Yr", "30 Yr"]

selected_maturities = st.multiselect(
    "Select Maturities to Plot:",
    options=all_maturities,
    default=["3 Mo", "2 Yr", "10 Yr"]
)

# --- Plotting Time Series ---
if selected_maturities:
    melted_df = filtered_df.melt(
        id_vars=["date"],
        value_vars=selected_maturities,
        var_name="Maturity",
        value_name="Yield (%)"
    )

    fig = px.line(
        melted_df,
        x="date",
        y="Yield (%)",
        color="Maturity",
        title="U.S. Treasury Yield Time Series",
        labels={"date": "Date", "Yield (%)": "Yield (%)"}
    )

    fig.update_layout(
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Yield (%)",
        legend_title="Maturity"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select at least one maturity from the dropdown above.")

# --- Data Table View ---
with st.expander("Show Data Table"):
    st.dataframe(filtered_df, use_container_width=True)

# fix the use_container_width warning

# modify so that e.g. .0324 displays as 3.24%
