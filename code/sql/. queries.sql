-- 1. Retrieve rows for region 'East' between two dates
SELECT *
FROM sales
WHERE region = 'East'
  AND date BETWEEN '2024-01-01' AND '2024-03-31'
ORDER BY date;

-- 2. Aggregate by category
SELECT category, COUNT(*) AS cnt, SUM(value) AS total_value, AVG(value) AS avg_value
FROM sales
GROUP BY category
HAVING COUNT(*) > 5
ORDER BY total_value DESC;

-- 3. Join example (if you have another table customers)
-- SELECT s.*, c.name
-- FROM sales s
-- JOIN customers c ON s.customer_id = c.id
-- WHERE c.segment = 'Enterprise';
