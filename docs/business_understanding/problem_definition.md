# Problem Definition

Although we do not have access to [Olist](https://olist.com)'s internal business metrics, the company operates at a large scale serving more than 50.000 customers and processing thousands of orders per day.

At this level, manually deriving insights becomes increasingly challenging, especially for tasks such as demand forecasting and customer segmentation.

## Goals

### Business Goals

- Identify patterns in historical sales data to support `demand forecasting`.
- Group customers into meaningful segments based on their purchasing behavior to support `customer segmentation`.
- Provide insights and interpretations that are understable and actionable for the business.

### Technical Goals

- Build an end-to-end Machine Learning pipeline, from data ingestion to model training and evaluation.
- Ensure the pipeline is reproducible and modular, enabling future extensions and improvements.
- Deploy the trained model and expose predictions through a simple web interface for demonstration purposes.

## Questions

1. `demand forecasting`: Based on historical sales data, how much demand can we expect at the product category level in the coming months?
2. `customer segmentation`: What types of customers can be identified based on their purchasing behavior and transaction history?
