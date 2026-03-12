# Explore Data

This step explores the data through queries, visualizations, and reports to answer business questions and identify patterns relevant to the machine learning goals.

---

### Business Questions

1. Do customers place enough orders (≥ 10)?
2. How concentrated is customer spending?
3. Do customers show preferences for specific sellers?
4. Are there distinct purchasing behaviors among customers?

---

1. Do customers place enough orders (≥ 10)?
   ![Distribution of Customers by Number of Orders](../images/Distribution%20of%20Customers%20by%20Number%20of%20Orders.png)
   **Answer:** No. Most customers placed only one order, just 1 customer with ID `8d50f5eadf50201ccdcedfb9e2ac8455` made 17 orders.

---

### Takeaways

The dataset shows insufficient order history per customer to support reliable customer segmentation. Most customers placed only one order, which limits the ability to model repeat purchasing behavior. Collecting additional order data would be necessary before proceeding with customer-level segmentation.
