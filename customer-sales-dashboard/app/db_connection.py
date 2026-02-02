import sqlite3
import pandas as pd

def get_connection(db_path='data/sales.db'):
    return sqlite3.connect(db_path)

def load_data_from_db(conn):
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    products_df = pd.read_sql_query("SELECT * FROM products", conn)
    sales_df = pd.read_sql_query("SELECT * FROM sales", conn)
    return customers_df, products_df, sales_df

def execute_query(conn, query):
    return pd.read_sql_query(query, conn)