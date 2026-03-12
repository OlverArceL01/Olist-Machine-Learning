# Clean Data

This step may involve selecting clean subsets of the data, inserting suitable default values, or applying techniques for handling missing values.

## 1. Product Category Name Missing Values

Based on the Describe Data step, no missing values were found in the following selected attributes:

- `orders.order_id`
- `orders.order_purchase_timestamp`
- `order_items.order_id`
- `order_items.order_item_id`
- `order_items.product_id`
- `order_items.price`
- `order_items.freight_value`
- `product_category_name_translation.product_category_name`
- `product_category_name_translation.product_category_name_english`

The only dataset containing missing values in selected fields is products, where: `product_id` contains no missing values
`product_category_name` contains 610 missing values, representing approximately 1.85% of the total product records.

Given the low proportion of missing values and the importance of use category information for filtering the missing values in `product_category_name` will be treated using a placeholder category label `missing`.

## 2. Order Items `price` and `freight_value` outlier values

During the Verify data quality step, extreme outliers were identified in the `order_items` dataset for `price` and `freight_value`.

Then, `order_items` records with `price > 8000` or `freight_value > 80` will be removed as part of the cleaning process.
