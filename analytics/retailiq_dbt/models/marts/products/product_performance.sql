select
    product_id,
    count(*) as total_orders,
    sum(quantity) as units_sold,
    sum(total_amount) as revenue
from {{ ref('stg_orders') }}
group by product_id
order by revenue desc