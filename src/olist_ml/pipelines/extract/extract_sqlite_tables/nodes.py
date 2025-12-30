import pandas as pd
from pathlib import Path
from sqlalchemy import Engine, create_engine
from olist_ml.pipelines.extract.extract_sqlite_tables.types import OutputPaths

def extract_sqlite_tables(
        input_path: Path,
        output_paths: OutputPaths):
    db_file = f"sqlite:///{input_path}"
    engine: Engine = create_engine(db_file)
    extract_sqlite_table(
        table_name="orders",
        output_path=output_paths.orders,
        columns=[
            'order_id',
            'customer_id',
            'order_status',
            'order_purchase_timestamp',
            'order_approved_at',
            'order_delivered_carrier_date',
            'order_delivered_customer_date',
            'order_estimated_delivery_date'
            ],
        engine=engine,
    )
    extract_sqlite_table(
        table_name="order_items",
        output_path=output_paths.order_items,
        columns=[
            'order_id',
            'order_item_id',
            'product_id',
            'seller_id', 
            'shipping_limit_date', 
            'price', 
            'freight_value'
            ],
        engine=engine,
    )
    extract_sqlite_table(
        table_name="products",
        output_path=output_paths.products,
        columns=[
            'product_id',
            'product_category_name',
            'product_name_lenght', 
            'product_description_lenght',
            'product_photos_qty',
            'product_weight_g',
            'product_length_cm',
            'product_height_cm',
            'product_width_cm'
            ],
        engine=engine,
    )
    extract_sqlite_table(
        table_name="customers",
        output_path=output_paths.customers,
        columns=[
            'customer_id',
            'customer_unique_id',
            'customer_zip_code_prefix',
            'customer_city',
            'customer_state'
            ],
        engine=engine,
    )
    extract_sqlite_table(
        table_name="product_category_name_translation",
        output_path=output_paths.product_category_name_translation,
        columns=[
            'product_category_name',
            'product_category_name_english'
            ],
        engine=engine,
    )

def extract_sqlite_table(
        output_path: Path, 
        table_name: str,
        columns: list[str], 
        engine: Engine):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    query = f"SELECT {', '.join(columns)} FROM {table_name};"
    table_data = pd.read_sql(query, engine)
    table_data.to_parquet(output_path, index=False)
