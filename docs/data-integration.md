# Data Integration

## Dataset Granularity

The dataset granularity is at the order item level, since each order item represents an instance where a specific customer selects a specific product for purchase, which is useful for `Demand Forecasting` and `Customer Segmentation`.

## Data Transformation

### Orders

- `order_status` was converted to a categorical `dtype` and `order_purchase_timestamp`, `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date`, `order_estimated_delivery_date` were parsed to a datetime.
- A small number of missing values 160 were found in `order_approved_at` 160 and were removed.
- `order_delivered_carrier_date`, `order_delivered_customer_date` and `order_estimated_delivery_date` were excluded, delivery information occurs after the purchase decision and may introduce noise in `Demand Forecasting` and `Customer Segmentation`.

### Order Items

- `shipping_limit_date` was discarded,as it refers to a delivery operation rather than the purchase process.
- `seller_id` was discarded, it is just and identifier.

### Products

- `product_name_lenght`, `product_description_lenght` and `product_photos_qty` were excluded, as they are more closely related to user experience and catalog quality.
- According to Kaggle dataset documentation `freight_value` already accounts for product weight and dimensions. Then `product_weight_g`, `product_length_cm`, `product_height_cm` and `product_width_cm` were discard, due to redundancy.
- `product_category_name` contained 610 missing values, were filled with a new category labeled `missing`.

### Customers

- `customer_zip_code_prefix` was excluded, as it provides similar information to `customer_city` and `customer_state`.
- `customer_city` and `customer_state` were converted to categorical `dtype`.

## Data Merging

- Tables are merged using left join, and identifier columns such as `order_id`, `order_item_id`, `seller_id`, `product_category_name` and `customer_id` were removed, as they do not add value for the modeling tasks.

## Post-Merge Validations

- `product_category_name_english`, `product_id`, `customer_unique_id` were converted to categorical `dtype`.
- `customer_unique_id` contained 15 missing values, which were removed.
- Columns names were updated for clarify and consistency:
  - `price` to `product_price`
  - `freight_value` to `shipping_cost`
  - `product_category_name_english` to `product_category_name`
  - `customer_unique_id` to `customer_id`
