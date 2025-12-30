import pandas as pd
from pathlib import Path
from typing import Callable
from olist_ml.pipelines.preprocessing.normalize_extracted_tables.types import OutputPaths, InputPaths

def normalize_extracted_tables(
        input_paths: InputPaths, 
        output_paths: OutputPaths):    
    normalize_extracted_table(
        table_name="orders",
        input_path=input_paths.orders, 
        output_path=output_paths.orders,
        normalize_fn=normalize_orders
    )
    normalize_extracted_table(
        table_name="order_items",
        input_path=input_paths.order_items,
        output_path=output_paths.order_items,
        normalize_fn=normalize_order_items
    )
    normalize_extracted_table(
        table_name="products",
        input_path=input_paths.products,
        output_path=output_paths.products,
        normalize_fn=normalize_products
    )
    normalize_extracted_table(
        table_name="customers",
        input_path=input_paths.customers,
        output_path=output_paths.customers,
        normalize_fn=normalize_customers
    )
    normalize_extracted_table(
        table_name="product_category_name_translation",
        input_path=input_paths.product_category_name_translation,
        output_path=output_paths.product_category_name_translation,
        normalize_fn=normalize_product_category_name_translation
    )

def normalize_extracted_table(
        input_path: Path,
        output_path: Path,
        normalize_fn: Callable[[pd.DataFrame], pd.DataFrame],
        table_name: str):
    df = pd.read_parquet(input_path)
    df = normalize_fn(df)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)

def normalize_orders(df: pd.DataFrame) -> pd.DataFrame:
    date_cols = [
        "order_purchase_timestamp", 
        "order_approved_at", 
        "order_delivered_carrier_date", 
        "order_delivered_customer_date", 
        "order_estimated_delivery_date"
    ]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])
    return df

def normalize_order_items(df: pd.DataFrame) -> pd.DataFrame:
    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"])
    return df

def normalize_products(df: pd.DataFrame) -> pd.DataFrame:
    return df

def normalize_customers(df: pd.DataFrame) -> pd.DataFrame:
    return df

def normalize_product_category_name_translation(df: pd.DataFrame) -> pd.DataFrame:
    return df