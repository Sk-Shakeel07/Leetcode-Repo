# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) as unit
FROM products p LEFT JOIN orders o ON p.product_id = o.product_id
WHERE order_date LIKE "2020-02%"
GROUP BY p.product_name
HAVING SUM(unit) >= 100