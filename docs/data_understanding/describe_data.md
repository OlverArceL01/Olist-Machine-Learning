# Describe Data

This step is used to examine the data and document its surface properties like data format, number of records, or field identities.

---

[E-commerce dataset by Olist (SQLite)
](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database) is composed by an SQLite database file, the majority information contained it is about orders made by customers, details about the orders items, who was the seller and the products related to the order all these information in the period 31/12/2016-30/08/2018.

---

## Entity-Relationship Diagram

The following Entity-Relationship Diagram is presented from the database in Kaggle.
![entity-relationship-diagram](../images/entity-relationship-diagram.png)

To give an idea about the number of rows between tables in the database. There are about 100.000 rows each customers, order items and orders tables.

---

## Datasets

### Orders

Order represent an instance of a customer made an order, then it can be used to track the order status and its dates.

- 99441 orders and 8 attributes.
- `order_id`: Primary key.
- `customer_id`: Foreign key from customers dataset.
- `order_status`: Step in which the order is, e.j `delivered`, `invoiced`, `shipped`, `processing`, `unavailable`, `canceled`, `created` and `approved`.
- The most frequently order state is `delivered` with 96478 orders.
- `order_purchase_timestamp`: Date when the order place at.
- `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date` and `order_estimated_delivery_date` are dates related to the order status probably for logistical purposes.

There are missing values, `order_approved_at` (160), `order_delivered_carrier_date` (1783), `order_delivered_customer_date` (2965).

Dates (`order_purchase_timestamp`, `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date`, `order_estimated_delivery_date`) are stored as objects data types, it is much more convenient to parsed them to a datetime data type.

Dates consider an acceptable range of time from september 2016 to october 2018 for the machine learning project goals.

### Order Items

Order item represent an item of product to add into the order, considering costs and a deadline to the seller.

- 112650 order items and 7 attributes.
- `order_item_id`: Sequential number to distinct and order item into the same order, it is not unique between all the orders.
- `order_id`: Foreign key from orders dataset.
- `seller_id`: Foreign key from sellers dataset.
- `product_id`: Foreign key from products dataset.
- `shipping_limit_date`: Deadline in which the seller must provide the package to the shipping company. it should be stored in a datetime data type.
- `price`, `freight_value`: `price` refers to the order item cost and `freight_value` refers to the item shipping cost (considering measures and weight).
- Kaggle dataset documentation indicate that the total order value is the sum of total of order items values and total of the freight values.
- Kaggle dataset documentation do not indicate directly the type of monetary value, so it is inferred due the ecommerce location Brazil that it is BRL Brazilian Real.

### Products

Product represent an instance of a product and details about metadata and physical attributes.

- 32951 products and 9 attributes.
- `product_id`: Primary key.
- `product_category_name`: Foreign key from the product category name translation dataset.
- `product_name_lenght`, `product_description_lenght`, `product_photos_qty`: Represent information about product details, these contain typos, `product_name_lenght` should be `product_name_length` and `product_description_lenght` should be `product_description_length`.
- `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm`: Represent measures and weight of the product in grams and centimeter.

There are missing values, `product_category_name` (610), `product_name_lenght` (610), `product_description_lenght` (610), `product_photos_qty` (610), `product_weight_g` (2), `product_length_cm` (2), `product_height_cm` (2) and `product_width_cm` (2).

Although `product_name_lenght`, `product_description_lenght`, `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm` are stored in float date type, these contain discrete values.

There are 73 product categories, the most frequent is `cama_mesa_baho` with 3029 products. Some divisions may be unclear e.j `electrodomesticos`, `electrodomesticos_2`, `casa_conforto` and `casa_conforto_2`.

### Customers

Customer represent an instance when a customer made an order including location details in that point.

- 99441 non unique customers and 5 attributes.
- `customer_id`: Primary key.
- `customer_unique_id`: Foreign key of an unknowing dataset of unique customers.
- `customer_zip_code_prefix`: Foreign key from geolocation dataset.
- `customer_zip_code_prefix`, `customer_city`, `customer_state`: Represent location of the customer at the instance that the customer made an order.

The municipality of Sao Paulo and Sao Paulo State are the most preferred between all the municipalities and states.

### Product Category Name Translation

A product category name translation represent a name translation in English correspond to a category product.

- 71 name translation of product cateogies, 2 attributes.
- `product_category_name`: Primary key.
- `product_category_name_english`: name translated in English.
- In the previous product section there were 73 unique product category names, so there are 2 untracked categories for name translation.
- `product_category_name_english` has the same problem with product section which is unclear descriptive names, e.j. `home_appliances`, `home_appliances_2`, `home_comfort_2` and `home_confort`.

### Order Payments

An order payment represent the way each order was paid, considering amount and methods.

- 103886 order payments and 5 attributes.
- `order_id`: Foreign key from orders dataset.
- `payment_sequential`: Sequential number of each payment for an order, it is non unique in the all order payments.
- `payment_type`: Is the payment method, e.j `credit_card`, `boleto`, `voucher`, `debit_card`, `not_defined`. The most frequently method used is `credit_card` with 76795 order payments.
- `payment_installments`: Represent the number of payment installments to pay for.
- `payment_value`: The transaction value, it is inferred to be in BRL Brazilian Real.

### Order Reviews

An order review is when someone made a review of the order adding comments and score.

- 99224 order reviews and 7 attributes.
- `review_id`: Primary key.
- `order_id`: Foreign key from orders dataset.
- `review_score`: Review score in which the better is 5.
- `review_comment_title`, `review_comment_message`: Review title and body.
- `review_creation_date`, `review_answer_timestamp`: When the review was sent and answered. these should be stored in datetime data types.

There are missing values, `review_comment_title` (87656) and `review_comment_message` (58247).

### Sellers

A seller refers to who want to seller their products and where is the seller location.

- 3095 sellers and 4 attributes.
- `seller_id`: Primary key.
- `seller_zip_code_prefix`: Foreign key from geolocation dataset.
- `seller_city`, `seller_state`: Represent the seller municipality and state.

### Geolocation

A geolocation represent geographical location data.

- 1000163 geolocations and 5 attributes.
- `geolocation_zip_code_prefix`: Primary key.
- `geolocation_lat`, `geolocation_lng`: Latitude and longitude coordinates.
- `geolocation_city`, `geolocation_state`: City and State.

### Leads Closed

A qualified lead complete a survey in which the survey ask for marketing, business and products details.

- 842 leads closed and 14 attributes.
- `mql_id`: Foreign key from leads qualified dataset.
- `seller_id`: Foreign key from sellers dataset.
- `sdr_id`: key for the sales development representative.
- `sr_id`: Key for the sales representative.
- `won_date`: Date when the deal was closed. it should be stored in a datetime data type.
- `business_segment`, `business_type`: `business_segment` is the marketing segment, `business_type` is the type of business or company model.
- `lead_type`, `lead_behaviour_profile`: `lead_type` is a classification of leads and `lead_behaviour_profile` is the type of behaviour profile according to the sales development representative.
- `has_company`, `has_gtin`: Whether the lead has company documentation and use barcode for products.
- `average_stock`: Average stock declared for the lead products.
- `declared_product_catalog_size`, `declared_monthly_revenue`: `declared_product_catalog_size` is the number of products the lead intends to list in the catalog, `declared_monthly_revenue` is the estimated monthly revenue expected.

There are missing values, `business_segment` (1), `lead_type` (6), `lead_behaviour_profile` (177), `has_company` (779), `has_gtin` (778), `average_stock` (776), `business_type` (10), `declared_product_catalog_size` (773).

### Leads Qualified

A lead fill a form and is filtered in order to get just the qualified leads.

- 8000 leads qualified and 4 attributes.
- `mql_id`: Primary key.
- `landing_page_id`: Key for the lead landing page.
- `first_contact_date`: Date of the first contact solicitation of the lead. it should be stored in a date realted data type.
- `origin`: Type of media were the lead was acquired.

There are missing values, `origin` (60).
