with views as (
    select count(*) as views
    from {{ ref('stg_product_views') }}
),

carts as (
    select count(*) as carts
    from {{ ref('stg_cart_events') }}
),

orders as (
    select count(*) as orders
    from {{ ref('stg_orders') }}
)

select
    views.views,
    carts.carts,
    orders.orders,
    round(carts.carts * 100.0 / nullif(views.views, 0), 2) as view_to_cart_rate,
    round(orders.orders * 100.0 / nullif(carts.carts, 0), 2) as cart_to_order_rate
from views, carts, orders