# Data Overview

[E-commerce dataset by Olist (SQLite)
](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database) datasets is related to an Brazilian e-commerce, and it's composed by an SQLite database file. It was made from other two Olist datasets in Kaggle ([Brazilian E-Commerce Public Dataset by Olist
](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), [Marketing Funnel by Olist](https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist)).
The majority information contained it's about orders made by customers, details about the orders items, who was the seller and the products related to the order.

---

## Entity-Relationship Diagram

The following Entity-Relationship Diagram is presented from the dataset in Kaggle.
![entity-relationship-diagram](./entity-relationship-diagram.png)

To give an idea about the number of rows between tables in dataset. There are about 100.000 rows each customers, order items and orders tables.

---

## Tables Overview

### Orders

Order has information about the status and dates about when something important happen to the order.

- Total numbers of orders is 99441.
- Order keep a reference of the Customer that make it.
- `order_status` should have a categorical `dtype`.
- `order_purchase_timestamp`, `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date` and `order_estimated_delivery_date` should have a datetime `dtype`.
- There are 8 `order_status` which are `delivered`, `shipped`, `canceled`, `unavailable`, `invoiced`, `processing`, `created`, `approved`.
- The most frequent status is `delivered` with a frequency of 96478.
- The following attributes have missing values `order_approved_at` (160), `order_delivered_carrier_date` (1783) and `order_delivered_customer_date` (2965).

### Order Items

Order item has a position within the order, the product price, the freight cost and a shipping limit date.

- Total numbers of order items is 112650.
- Order items keep a reference of the order, including the position `order_item_id` of each order item to the order.
- Order items keep a reference of the product added.
- There is an instruction to calculate the total order amount from `price` and `freight_value` into the Kaggle dataset documentation.
- `shipping_limit_date` should have a datetime `dtype`.
- `price` and `freight_value` have outlier values, a few order items have a high cost $6735 BRL and $409.68 BRL respectively. But the majority of orders are less than $1000 BRL and $100 BRL respectively.
- Counting by `order_item_id`, there are outlier values, a few order have between 7 and 21 order items. But the majority of orders have just one order item.

### Products

Product has a category name, then product description details and physical attributes.

- Total numbers of products is 32951.
- `product_category_name` keeps a reference of Product category name translation table to read the category names in English.
- There are very specific information such as `product_name_lenght`, `product_description_lenght`, `product_photos_qty` about the product description, but it doesn't have any attribute about the product name or title, so it's necessary to referred the product by its `product_id`.
- There are physical attributes such as `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm`.
- `product_category_name` should be in English and have a categorical `dtype`.
- There are 73 unique product categories.
- Top 10 product categories just represent the 62.96%.
- There are missing values `product_category_name` (610), `product_name_lenght` (610), `product_description_lenght` (610), `product_photos_qty` (610), `product_weight_g` (2), `product_length_cm` (2), `product_height_cm` (2) and `product_width_cm` (2).

### Customers

Customer has a customer unique identifier and geographical attributes.

- Total numbers of customers is 99441 which is the same of the numbers of orders, every order has its proper instance of the customer, whether or not the customer is the same, so it's important to use `customer_unique_id` and finally there are 96096 unique customers.
- There are geographical attributes about where the customer make the order, `customer_zip_code_prefix`, `customer_city` and `customer_state`.
- There are outlier values of number of orders which they are between 4 and 17 times. But the majority of customers ordered just one time.
- There are 4119 cities and 27 states.
- The city with the highest number of orders is Sao Paulo city (15540), and the state with the largest number of orders is State of Sao Paulo (41746).

### Product Category Name Translation

Product Category Name Translation contain the translation of every product category name in English.

- Total numbers of product category name translation is 71, but previously in the section of product table, it was possible to count 73 unique product categories.
- Two product categories don't have a name translation, which are `pc_gamer` and `portateis_cozinha_e_preparadores_de_alimentos`.
