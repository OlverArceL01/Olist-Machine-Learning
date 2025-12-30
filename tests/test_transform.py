# import pandas as pd
# from e_commerce_ml_project.pipelines.integration.transforms import clean_olist_dataset

# def test_clean_olist_dataset_drops_missing_customers():
#     df = pd.DataFrame({
#         "customer_unique_id": [None, "A"],
#         "customer_id": ["c0", "c1"],
#         "product_id": ["p1", "p2"],
#         "product_category_name_english": ["cat", None],
#         "price": [10, 20],
#         "freight_value": [1, 2],
#         "order_id": [1, 2],
#         "order_item_id": [1, 2],
#         "seller_id": ["s1", "s2"],
#         "product_category_name": ["cat1", "cat2"],
#     })
    
#     result = clean_olist_dataset(df)

#     assert "customer_unique_id" not in result.columns
#     assert result["product_price"].tolist() == [20]