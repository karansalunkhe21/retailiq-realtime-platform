select
    event_id,
    customer_id,
    product_id,
    store_id,
    quantity,
    price,
    total_amount,
    timestamp as order_timestamp

from RETAILIQ.RAW.ORDERS