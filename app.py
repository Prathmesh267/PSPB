import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
@st.cache_data
def load_data():
    # Replace with your actual CSV/Excel file path or data
    df = pd.read_excel("Megacap_PSPB.xlsx",sheet_name= "Sheet2")  # or pd.read_excel("your_file.xlsx")
    return df

df = load_data()

# Title
st.title("📊 Company Financial Dashboard")

# Sidebar - Company selector
companies = df['Company'].unique()
selected_company = st.sidebar.selectbox("Select a Company", companies)

# Filter data
filtered_df = df[df['Company'] == selected_company]

# Show raw table
st.subheader(f"Data for {selected_company}")
st.dataframe(filtered_df)

# Plotting Section
st.subheader("📈 Financial Metrics Over Time")

metrics = ['MCAP', 'Net_Debt', 'ROCE', 'Revenue', 'PS+PB']
selected_metrics = st.multiselect("Select metrics to plot", metrics, default=['MCAP', 'ROCE'])

if selected_metrics:
    fig, ax = plt.subplots(figsize=(10, 5))
    for metric in selected_metrics:
        ax.plot(filtered_df['Year'], filtered_df[metric], marker='o', label=metric)
    ax.set_xlabel("Year")
    ax.set_title(f"{selected_company} - Financial Trends")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Select at least one metric to display a chart.")

