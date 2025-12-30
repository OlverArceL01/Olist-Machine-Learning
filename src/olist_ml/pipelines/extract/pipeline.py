from pathlib import Path
from olist_ml.config import OlistConfig
from olist_ml.pipelines.extract.download_sqlite_from_gcs.nodes import download_sqlite_from_gcs
from olist_ml.pipelines.extract.extract_sqlite_tables.nodes import extract_sqlite_tables
from olist_ml.pipelines.extract.download_sqlite_from_gcs import types as download_types
from olist_ml.pipelines.extract.extract_sqlite_tables import types as extract_types

def run_pipeline(cfg: OlistConfig) -> None:
    raw_data_path = Path(cfg.project.root_path) / cfg.paths.raw_data

    download_sqlite_from_gcs(
        input_path=cfg.project.google_cloud.source_blob,
        output_path=download_types.OutputPaths(
            zip_path= raw_data_path / cfg.files.olist_zip,
            sqlite_path= raw_data_path / cfg.files.olist_sqlite,
        ),
        bucket_name=cfg.project.google_cloud.bucket_name
    )
    extract_sqlite_tables(
        input_path=raw_data_path / cfg.files.olist_sqlite,
        output_paths=extract_types.OutputPaths(
            orders=raw_data_path / cfg.files.orders_extract_parquet,
            order_items=raw_data_path / cfg.files.order_items_extract_parquet,
            products=raw_data_path / cfg.files.products_extract_parquet,
            customers=raw_data_path / cfg.files.customers_extract_parquet,
            product_category_name_translation=raw_data_path / cfg.files.product_category_name_translation_extract_parquet
    ))