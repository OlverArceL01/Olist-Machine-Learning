from dataclasses import dataclass


@dataclass(frozen=True)
class GoogleCloud:
    project_id: str
    bucket_name: str
    source_blob: str

@dataclass(frozen=True)
class Project:
    root_path: str
    google_cloud: GoogleCloud

@dataclass(frozen=True)
class Paths:
  raw_data: str
  interim_data: str
  processed_data: str
  models_data: str
  external_data: str

@dataclass(frozen=True)
class Files:
    olist_zip: str
    olist_sqlite: str

    orders_extract_parquet: str
    order_items_extract_parquet: str
    products_extract_parquet: str
    customers_extract_parquet: str
    product_category_name_translation_extract_parquet: str

    orders_normalize_parquet: str
    order_items_normalize_parquet: str
    products_normalize_parquet: str
    customers_normalize_parquet: str
    product_category_name_translation_normalize_parquet: str
    base_dataset_parquet: str

@dataclass(frozen=True)
class OlistConfig:
    project: Project
    paths: Paths
    files: Files