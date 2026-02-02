import pandas as pd

def calculate_kpis(sales_df):
    total_sales = sales_df['total_amount'].sum()
    total_orders = len(sales_df)
    avg_order = sales_df['total_amount'].mean()
    return total_sales, total_orders, avg_order

def filter_by_date(sales_df, start_date, end_date):
    sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
    return sales_df[(sales_df['sale_date'] >= start_date) & (sales_df['sale_date'] <= end_date)]