
select 
 date_trunc('day', order_timestamp) as date,
 sum(total_amount) as revenue,
 count(*) as total_orders,
 sum(quantity) as total_items_sold,
 from {{ ref('stg_orders') }} 
 group by date
 order by date