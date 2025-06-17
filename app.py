import streamlit as st
import pandas as pd
import altair as alt
import openpyxl
# Load your data
@st.cache_data
def load_data():
    df = pd.read_excel("Megacap_PSPB.xlsx", sheet_name="Sheet2",engine="openpyxl")
    return df

df = load_data()

st.title("📊 Company Financial Dashboard")

companies = df['Company'].unique()
selected_company = st.sidebar.selectbox("Select a Company", companies)

filtered_df = df[df['Company'] == selected_company]

st.subheader(f"Data for {selected_company}")
st.dataframe(filtered_df)

st.subheader("📈 Financial Metrics Over Time")

metrics = ['MCAP', 'Net_Debt', 'ROCE', 'Revenue', 'PS+PB']
selected_metrics = st.multiselect("Select metrics to plot", metrics, default=['MCAP', 'ROCE'])

if selected_metrics:
    chart_df = filtered_df[['Year'] + selected_metrics].melt('Year', var_name='Metric', value_name='Value')
    chart = alt.Chart(chart_df).mark_line(point=True).encode(
        x='Year:O',
        y='Value:Q',
        color='Metric:N'
    ).properties(width=700, height=400, title=f"{selected_company} - Financial Trends")
    st.altair_chart(chart)
else:
    st.info("Select at least one metric to display a chart.")
