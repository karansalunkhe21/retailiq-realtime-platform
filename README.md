
# RetailIQ – Real-Time Retail Intelligence Platform

## Overview

RetailIQ is an end-to-end data engineering and analytics project that simulates retail transactions, streams events through Apache Kafka, ingests data into Snowflake, transforms data using dbt, and visualizes key business metrics in Power BI.

The project demonstrates how modern data platforms process real-time events and convert raw transactional data into actionable business insights.

## Business Problem

Retail organizations generate thousands of transactions across stores and channels every day. Business teams require near real-time visibility into revenue, orders, customer activity, and product performance.

RetailIQ simulates this workflow by creating a streaming analytics platform capable of:

* Capturing retail transaction events
* Streaming events through Kafka
* Loading data into Snowflake
* Transforming data using dbt
* Delivering executive insights through Power BI

---

## Architecture

```text
CSV Seed Data
      │
      ▼
Python Event Simulator
      │
      ▼
Apache Kafka
      │
      ▼
Snowflake Data Warehouse
      │
      ▼
dbt Transformations
      │
      ▼
Power BI Dashboard
```

---

## Technology Stack

| Layer            | Technology   |
| ---------------- | ------------ |
| Programming      | Python       |
| Streaming        | Apache Kafka |
| Containerization | Docker       |
| Data Warehouse   | Snowflake    |
| Transformations  | dbt          |
| Analytics        | SQL          |
| Visualization    | Power BI     |
| Version Control  | Git & GitHub |

---

## Project Structure

```text
retailiq-realtime-platform/
│
├── simulator/
│   ├── kafka_producer.py
│   ├── customers_generator.py
│   ├── products_generator.py
│   └── stores_generator.py
│
├── data/
│   └── seeds/
│       ├── customers.csv
│       ├── products.csv
│       └── stores.csv
│
├── snowflake/
│   └── ingestion_scripts/
│
├── analytics/
│   └── retailiq_dbt/
│       ├── models/
│       ├── seeds/
│       └── macros/
│
├── powerbi/
│   └── RetailIQ_Dashboard.pbix
│
├── docs/
│   ├── architecture.png
│   └── dashboard.png
│
├── docker-compose.yml
│
└── README.md
```

---

## Data Flow

### 1. Seed Data Generation

Reference datasets are generated for:

* Customers
* Products
* Stores

These datasets act as master data used during event simulation.

### 2. Event Simulation

A Python producer generates retail transaction events including:

* Order ID
* Customer ID
* Product ID
* Store ID
* Quantity
* Revenue
* Timestamp

### 3. Event Streaming

Events are published to Kafka topics where they are processed as streaming records.

### 4. Snowflake Ingestion

Kafka events are loaded into Snowflake raw tables for storage and analytics.

### 5. Data Transformation

dbt models transform raw transaction data into analytics-ready datasets.

### 6. Business Intelligence

Power BI connects to Snowflake and presents executive-level KPIs and visualizations.

---

## Key Metrics

The dashboard tracks:

* Total Revenue
* Total Orders
* Average Order Value (AOV)
* Total Items Sold
* Product Performance
* Revenue Distribution
* Conversion Funnel Analysis

---

## Dashboard

The Power BI Executive Dashboard provides a centralized view of retail performance.

Key visualizations include:

* Revenue KPI
* Orders KPI
* Average Order Value KPI
* Items Sold KPI
* Revenue by Product
* Top Products Analysis
* Customer Conversion Funnel

---

## Skills Demonstrated

### Data Engineering

* Event-driven architecture
* Real-time data streaming
* ETL/ELT pipeline design
* Data warehouse integration

### Analytics Engineering

* dbt transformations
* Data modeling
* Business metric development

### Business Intelligence

* KPI design
* Dashboard development
* Executive reporting

### Cloud Data Platforms

* Snowflake
* Kafka
* Docker

---

## Future Enhancements

Potential future improvements include:

* Historical data generation
* Product categories and brands
* Airflow orchestration
* Data quality monitoring
* Customer segmentation
* Real-time alerting
* Predictive analytics

---

## Author

Karan Salunkhe

MS Information Systems
Syracuse University

