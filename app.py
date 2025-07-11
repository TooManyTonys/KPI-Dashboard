import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Sales KPI Dashboard")

# Upload CSV file widget
uploaded_file = st.file_uploader("Drag and drop your sales data CSV here", type=["csv"])

if uploaded_file:
    # Read CSV file into DataFrame
    df = pd.read_csv(uploaded_file)

    # Basic data checks
    st.write("Preview of your data:")
    st.dataframe(df.head())

    # Check if essential columns exist
    required_cols = {'Date', 'Sales Amount', 'Units Sold', 'Region'}
    if not required_cols.issubset(df.columns):
        st.error(f"Your file must contain these columns: {required_cols}")
    else:
        # Process Date
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])  # drop rows where date could not parse
        df['Month'] = df['Date'].dt.to_period('M').astype(str)

        # Calculate KPIs
        total_sales = df['Sales Amount'].sum()
        avg_order_value = df['Sales Amount'].mean()
        units_sold = df['Units Sold'].sum()

        # Display KPIs
        st.metric("Total Sales", f"${total_sales:,.2f}")
        st.metric("Average Order Value", f"${avg_order_value:,.2f}")
        st.metric("Units Sold", f"{units_sold}")

        # Sales over time chart
        sales_over_time = df.groupby('Month')['Sales Amount'].sum().reset_index()
        fig = px.line(sales_over_time, x='Month', y='Sales Amount', title='Sales Over Time')
        st.plotly_chart(fig)

        # Sales by Region
        sales_by_region = df.groupby('Region')['Sales Amount'].sum().reset_index()
        fig2 = px.bar(sales_by_region, x='Region', y='Sales Amount', title='Sales by Region')
        st.plotly_chart(fig2)

else:
    st.info("Please upload a CSV file containing sales data with columns: Date, Sales Amount, Units Sold, Region.")
