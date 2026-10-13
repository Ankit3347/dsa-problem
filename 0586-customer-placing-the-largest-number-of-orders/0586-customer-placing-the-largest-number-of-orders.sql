/* Write your T-SQL query statement below */

WITH CustomerOrders AS (
    SELECT
        customer_number,
        COUNT(order_number) AS total_orders
    FROM Orders
    GROUP BY customer_number
)
SELECT customer_number
FROM CustomerOrders
WHERE total_orders = (
    SELECT MAX(total_orders)
    FROM CustomerOrders
);
