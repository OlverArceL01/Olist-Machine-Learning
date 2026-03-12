# Olist E-commerce Machine Learning Documentation

![olist](./images/olist.jpg)

## Introduction

E-commerce businesses today can leverage Machine Learning to uncover valuable insights from `demand forecasting` to `customer segmentation` and more.  
This documentation presents the application of Machine Learning techniques to common problems found in some e-commerce platforms.

## Dataset Overview

This project uses the public [Olist e-commerce dataset](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database) from Kaggle.
It contains ~100k orders, customer information, product details, sellers, and delivery performance across multiple relational tables between 31/12/2016 and 30/08/2018 in Brazil.

## Table of Contents

This documentation follows the full Machine Learning workflow for the Olist dataset:

### Business Understanding:

1. [Problem Definition](./business_understanding/problem_definition.md) – Define project goals and questions.

### Data Understanding:

1. [Describe Data](./data_understanding/describe_data.md) – High-level overview of the data structure.
2. [Explore Data Demand Forecasting](./data_understanding/explore_data_demand_forecasting.md) - Business-driven exploration focused on answering key questions and identifying relevant patterns.
3. [Explore Data Customer Segmentation](./data_understanding/explore_data_customer_segmentation.md) - Business-driven exploration focused on answering key questions and identifying relevant patterns.
4. [Verify Data Quality](./data_understanding/verify_data_quality.md) - How clean/dirty is the data.

### Data Preparation

5. [Select Data](./data_preparation/select_data.md) – Choose relevant features and target variables, with rationale for inclusion/exclusion.
6. [Clean Data](./data_preparation/clean_data.md) - Handle missing values, outliers, duplicates, and data type errors.
7. [Construct Data](./data_preparation/construct_data.md) - Create new features or derived attributes to improve model performance.
8. [Format Data](./data_preparation/format_data.md) - Transform and encode data for ML models (scaling, encoding, reshaping).

### Modeling

[Modeling](./modeling/modeling.md) – ML model selection and training.

### Evaluation

[Evaluation](./evaluation/evaluation.md) – Metrics, validation, and analysis of results.

### Deployments

[Deployment](./deployment/deployment.md) – Packaging models, pipelines, and reproducibility.
