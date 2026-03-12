# Select Data

This step identifies and selects relevant datasets, records, and attributes that will be used for modeling and analysis tasks.

## Selected Datasets

The following datasets are selected:

- `orders`: Provides `order_purchase_timestamp`, which allows us to identify when each order was created, It is essential for establishing the temporal dimension of the analysis. `order_id` and `order_purchase_timestamp` are selected.
- `order_items`: Provides `price` and `freight_value` that together keep a positive correlation with the demand volume. Then only `order_items` whose product category contain 3000 order items or more are selected, in order to avoid including low-volume categories that do not provide enought data. `order_id`, `order_item_id`, `product_id`, `price` and `freight_value` are selected.
- `products`: Provides `product_category_name` to filter demand by category level groups. `product_id` and `product_category_name` are selected.
- `product_category_name_translation`: Provides `product_category_name_translation` to get the English translation of the product categories. `product_category_name` and `product_category_name_english` are selected.

## Unselected Datasets

The following datasets are not selected:

- `order_payments`: Payments are recorded at order level, not at order item level. There is no traceability between payments and individual products, which may introduce noise.
- `order_reviews`: Reviews are recorded at order level, not at order item level, and may introduce noise.
- `sellers`: Seller location information is highly imbalanced across cities and states.
- `customers`: Customer location information shows similar imbalance issues.
- `geolocation`: Imbalanced when combined with sellers and customers.
- `leads_qualified`: Data relates to the lead capture process and has no direct relationship with order items.
- `leads_closed`: Similar to `leads_qualified`.
