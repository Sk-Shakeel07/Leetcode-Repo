# Write your MySQL query statement below

select s.name
from SalesPerson s
left join Orders o
on s.sales_id = o.sales_id
left join Company c
on c.com_id = o.com_id
group by s.name 
having coalesce(sum(c.name = 'Red'), 0) = 0;
