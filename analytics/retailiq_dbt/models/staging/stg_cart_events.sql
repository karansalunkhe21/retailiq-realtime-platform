select
    event_id,
    customer_id,
    product_id,
    store_id,
    timestamp as cart_timestamp

from RETAILIQ.RAW.CART_EVENTS