# Explore Data

This step explores the data through queries, visualizations, and reports to answer business questions and identify patterns relevant to the machine learning goals.

---

### Business Questions

1. Do any products have sufficient order item volume (≥ 3,000)?
2. Do any product categories have sufficient order item volume (≥ 3,000)?
3. How does demand behave over time at the product category level (stability and seasonality)?
4. How do price and freight cost variations relate to demand?
5. How strong is the positive correlation between total cost and order item demand?

---

1. Do any products have sufficient order item volume (≥ 3,000)?
   No products reach the minimum threshold of 3.000 order items, making demand forecasting at this level infeasible.

2. Do any product categories have sufficient order item volume (≥ 3,000)?
   Out of 74 categories, 14 have sufficient order item volume (≥ 3.000), enabling analysis at this aggregation level.

3. How does demand behave over time at the product category level (stability and seasonality)?
   ![Demand over time for Selected Product Categories](../images/Demand%20over%20time%20for%20Selected%20Product%20Categories.png)
   Demand at the product category level is generally stable, with a noticeable seasonal increase between October 2017 and January 2018, likely related to end-of-year events.

4. How do price and freight cost variations relate to demand?
   ![Cost over time for Selected Product Categories](../images/Cost%20over%20time%20for%20Selected%20Product%20Categories.png)
   Total order item cost and price show a strong positive correlation with monthly demand. Freight cost remains relatively stable over time.

5. How strong is the positive correlation between total cost and order item demand?
   ![Normalized Order Cost vs Order Count by Product Category](../images/Normalized%20Order%20Cost%20vs%20Order%20Count%20by%20Product%20Category.png)
   There is a strong positive correlation between total order item cost and the number of order items per month.

---

### Takeaways

1. Demand forecasting at the **product level** is not feasible due to the low number of order items (≤ 3,000).
2. Demand forecasting at the **product category level** is possible for 14 categories that have ≥ 3,000 order items.
3. Demand at the product category level is **stable** and shows **seasonal patterns**, especially around end-of-year celebrations.
4. Total order item costs and total price have a **positive correlation** with the monthly demand of product categories.
5. This positive correlation is **strong**, resulting in **lower variations** across months.
