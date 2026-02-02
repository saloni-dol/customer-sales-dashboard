-- KPI and Reporting Queries

-- Total Sales
SELECT SUM(total_amount) AS total_sales FROM sales;

-- Sales by Product
SELECT p.name, SUM(s.total_amount) AS sales
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY sales DESC;

-- Top Customers
SELECT c.name, SUM(s.total_amount) AS total_spent
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 10;

-- Monthly Sales
SELECT strftime('%Y-%m', sale_date) AS month, SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;