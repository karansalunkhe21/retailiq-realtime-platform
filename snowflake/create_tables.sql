CREATE DATABASE IF NOT EXISTS RETAILIQ;

CREATE SCHEMA IF NOT EXISTS RETAILIQ.RAW;


CREATE SCHEMA IF NOT EXISTS RETAILIQ.ANALYTICS;


CREATE TABLE IF NOT EXISTS RETAILIQ.RAW.PRODUCT_VIEWS (
    event_id STRING,
    event_type STRING,
    customer_id STRING,
    product_id STRING,
    store_id STRING,
    timestamp TIMESTAMP
);


CREATE TABLE IF NOT EXISTS RETAILIQ.RAW.CART_EVENTS (
    event_id STRING,
    event_type STRING,
    customer_id STRING,
    product_id STRING,
    store_id STRING,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS RETAILIQ.RAW.ORDERS (
    event_id STRING,
    customer_id STRING,
    product_id STRING,
    store_id STRING,
    quantity INT,
    price FLOAT,
    total_amount FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS RETAILIQ.RAW.RETURNS (
    event_id STRING,
    customer_id STRING,
    product_id STRING,
    store_id STRING,
    reason STRING,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS RETAILIQ.RAW.INVENTORY_ALERTS (
    event_type STRING,
    product_id STRING,
    remaining_qty INT,
    timestamp TIMESTAMP
);

SELECT COUNT(*) FROM RETAILIQ.RAW.ORDERS;
SELECT COUNT(*) FROM RETAILIQ.RAW.PRODUCT_VIEWS;
SELECT COUNT(*) FROM RETAILIQ.RAW.RETURNS;