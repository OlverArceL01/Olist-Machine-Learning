import pandas as pd
from pathlib import Path
from pandas_gbq import to_gbq
from google.cloud import bigquery
from google.cloud import bigquery_storage
from olist_ml.pipelines.preprocessing.build_base_dataset_in_bigquery.types import InputPaths

def build_base_dataset_in_bigquery(
        input_paths: InputPaths, 
        output_path: Path,
        project_id: str
        ):
    client = bigquery.Client(project=project_id)
    bqstorage_client = bigquery_storage.BigQueryReadClient()
    dataset = "olist_tables"
    # upload_tables_to_bigquery(
    #     dataset=dataset,
    #     input_paths=input_paths,
    #     project_id=project_id
    # )
    query = f"""
        SELECT
            ord.order_id,
            oi.order_item_id,
            oi.product_id,
            oi.price,
            oi.freight_value,
            pr.product_category_name,
            pc.product_category_name_english,
            cus.customer_id,
            ord.order_status,
            ord.order_purchase_timestamp,
            ord.order_approved_at,
            cus.customer_unique_id,
            cus.customer_city,
            cus.customer_state
        FROM `{project_id}.{dataset}.order_items` oi
        LEFT JOIN `{project_id}.{dataset}.products` pr
            ON oi.product_id = pr.product_id
        LEFT JOIN `{project_id}.{dataset}.product_category_name_translation` pc
            ON pr.product_category_name = pc.product_category_name
        LEFT JOIN `{project_id}.{dataset}.orders` ord
            ON oi.order_id = ord.order_id
        LEFT JOIN `{project_id}.{dataset}.customers` cus
            ON ord.customer_id = cus.customer_id
        """
    base_dataset = client.query(query).to_dataframe(bqstorage_client)
    base_dataset.to_parquet(output_path, index=False)
    # import time
    # job = client.query(query)
    # while not job.done():
    #     print(f"Estado: {job.state}")
    #     time.sleep(2)
    # print("Query finalizada")
    # df = job.to_dataframe(bqstorage_client=bqstorage_client)

    # job = client.query(query)
    # print("Job ID:", job.job_id)
    # print("Estado inicial:", job.state)
    # job.result()  # espera a que termine
    # print("Estado final:", job.state)
    # df = job.to_dataframe(bqstorage_client=bqstorage_client)



def upload_tables_to_bigquery(dataset: str, input_paths: InputPaths, project_id: str):
    upload_table_to_bigquery(
        table_name="orders",
        dataset=dataset,
        input_path=input_paths.orders,
        project_id=project_id
    )
    upload_table_to_bigquery(
        table_name="order_items",
        dataset=dataset,
        input_path=input_paths.order_items,
        project_id=project_id
    )
    upload_table_to_bigquery(
        table_name="products",
        dataset=dataset,
        input_path=input_paths.products,
        project_id=project_id
    )
    upload_table_to_bigquery(
        table_name="customers",
        dataset=dataset,
        input_path=input_paths.customers,
        project_id=project_id
    )
    upload_table_to_bigquery(
        table_name="product_category_name_translation",
        dataset=dataset,
        input_path=input_paths.product_category_name_translation,
        project_id=project_id
    )

def upload_table_to_bigquery(
        table_name: str,
        dataset: str,
        input_path: Path,
        project_id,
):
    to_gbq(
        dataframe=pd.read_parquet(input_path),
        destination_table=f"{dataset}.{table_name}",
        project_id=project_id,
        if_exists="replace"
    )