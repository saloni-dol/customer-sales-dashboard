import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("Customer Sales Dashboard")

# Load data
@st.cache_data
def load_data():
    # Assuming data is in processed folder or from DB
    sales_df = pd.read_csv('data/processed/sales_cleaned.csv')
    customers_df = pd.read_csv('data/processed/customers_cleaned.csv')
    products_df = pd.read_csv('data/processed/products_cleaned.csv')
    return sales_df, customers_df, products_df

sales_df, customers_df, products_df = load_data()

# Sidebar
st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox("Product Category", products_df['category'].unique())

# Filter data
filtered_sales = sales_df[sales_df['product_id'].isin(products_df[products_df['category'] == selected_category]['product_id'])]

# KPIs
st.header("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_sales['total_amount'].sum():,.2f}")
col2.metric("Total Orders", len(filtered_sales))
col3.metric("Average Order Value", f"${filtered_sales['total_amount'].mean():,.2f}")

# Charts
st.header("Sales Over Time")
fig = px.line(filtered_sales.groupby('sale_date')['total_amount'].sum().reset_index(), x='sale_date', y='total_amount')
st.plotly_chart(fig)

st.header("Top Products")
top_products = filtered_sales.groupby('product_id')['total_amount'].sum().nlargest(10).reset_index()
top_products = top_products.merge(products_df, on='product_id')
fig2 = px.bar(top_products, x='name', y='total_amount')
st.plotly_chart(fig2)