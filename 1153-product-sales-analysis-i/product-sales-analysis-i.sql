-- Get product details along with year and price
WITH SaleDetails AS (
    SELECT
        p.product_name,
        s.year,
        s.price
    FROM Sales s
    JOIN Product p ON s.product_id = p.product_id
)
SELECT * FROM SaleDetails;
