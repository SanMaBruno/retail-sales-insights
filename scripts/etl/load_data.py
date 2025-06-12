import pandas as pd
import os

RAW_PATH = 'data/raw'

def load_csv(name):
    path = os.path.join(RAW_PATH, name)
    return pd.read_csv(path)

if __name__ == "__main__":
    df_customers = load_csv("olist_customers_dataset.csv")
    print("Clientes:", df_customers.shape)

    df_orders = load_csv("olist_orders_dataset.csv")
    print("Órdenes:", df_orders.shape)