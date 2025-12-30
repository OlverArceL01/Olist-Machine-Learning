from pathlib import Path
from olist_ml.config import OlistConfig
from olist_ml.pipelines.preprocessing.normalize_extracted_tables.nodes import normalize_extracted_tables
from olist_ml.pipelines.preprocessing.build_base_dataset_in_bigquery.nodes import build_base_dataset_in_bigquery
from olist_ml.pipelines.preprocessing.normalize_extracted_tables import types as normalize_types
from olist_ml.pipelines.preprocessing.build_base_dataset_in_bigquery import types as build_base_dataset_types

def run_pipeline(cfg: OlistConfig) -> None:
    raw_data_path = Path(cfg.project.root_path) / cfg.paths.raw_data
    interim_data_path = Path(cfg.project.root_path) / cfg.paths.interim_data
    normalize_extracted_tables(
        input_paths=normalize_types.InputPaths(
            orders=raw_data_path / cfg.files.orders_extract_parquet,
            order_items=raw_data_path / cfg.files.order_items_extract_parquet,
            products=raw_data_path / cfg.files.products_extract_parquet,
            customers=raw_data_path / cfg.files.customers_extract_parquet,
            product_category_name_translation=raw_data_path / cfg.files.product_category_name_translation_extract_parquet
        ),
        output_paths=normalize_types.OutputPaths(
            orders=interim_data_path / cfg.files.orders_normalize_parquet,
            order_items=interim_data_path / cfg.files.order_items_normalize_parquet,
            products=interim_data_path / cfg.files.products_normalize_parquet,
            customers=interim_data_path / cfg.files.customers_normalize_parquet,
            product_category_name_translation=interim_data_path / cfg.files.product_category_name_translation_normalize_parquet
        )
    )
    build_base_dataset_in_bigquery(
        input_paths= build_base_dataset_types.InputPaths(
            orders=interim_data_path / cfg.files.orders_normalize_parquet,
            order_items=interim_data_path / cfg.files.order_items_normalize_parquet,
            products=interim_data_path / cfg.files.products_normalize_parquet,
            customers=interim_data_path / cfg.files.customers_normalize_parquet,
            product_category_name_translation=interim_data_path / cfg.files.product_category_name_translation_normalize_parquet
        ),
        output_path=interim_data_path / cfg.files.base_dataset_parquet,
        project_id=cfg.project.google_cloud.project_id
    )