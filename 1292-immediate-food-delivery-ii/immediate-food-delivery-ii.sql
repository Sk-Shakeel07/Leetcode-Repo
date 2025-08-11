# Write your MySQL query statement below
WITH tb1 AS (
    SELECT
      customer_id,
      MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY customer_id
)

select
round(sum(d.order_date = d.customer_pref_delivery_date) / count(*) * 100 ,2)
as immediate_percentage 
from Delivery as d
join tb1
on d.customer_id = tb1.customer_id and d.order_date = tb1.min_order_date 