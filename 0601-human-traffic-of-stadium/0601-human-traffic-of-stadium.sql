/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
valid_groups AS (
    SELECT grp
    FROM cte
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT id,
       visit_date,
       people
FROM cte
WHERE grp IN (
    SELECT grp
    FROM valid_groups
)
ORDER BY visit_date;