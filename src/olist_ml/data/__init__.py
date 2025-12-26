import logging
from olist_ml.data.extract import extract
from olist_ml.data.save import save
from olist_ml.data.transform import transform

def main():
    logger = logging.getLogger(__name__)
    logger.info("loading raw data...")
    extract()
    transform()
    save()