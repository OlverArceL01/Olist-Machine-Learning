import zipfile
from tqdm import tqdm
from google.cloud import storage
from olist_ml.pipelines.extract.download_sqlite_from_gcs.types import OutputPaths

def download_sqlite_from_gcs(input_path: str, output_paths: OutputPaths, bucket_name: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(input_path)
    blob.reload()
    total_size = blob.size
    chunk_size = 1*1024*1024

    with open(output_paths.zip_path, "wb") as f, tqdm(total=total_size, unit='B', unit_scale=True, desc=input_path) as pbar:
        for start in range(0, total_size, chunk_size):
            end = min(start + chunk_size - 1, total_size - 1)
            f.write(blob.download_as_bytes(start=start, end=end))
            pbar.update(end - start + 1)  

    with zipfile.ZipFile(output_paths.zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_paths.zip_path.parent)