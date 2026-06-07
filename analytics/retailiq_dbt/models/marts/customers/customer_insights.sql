select
    customer_id,
    count(*) as total_orders,
    sum(total_amount) as lifetime_value,
    avg(total_amount) as avg_order_value
from {{ ref('stg_orders') }}
group by customer_id