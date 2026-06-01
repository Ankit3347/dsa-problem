CREATE FUNCTION dbo.getNthHighestSalary (@N INT)
RETURNS INT
AS
BEGIN
    DECLARE @Result INT;

    SELECT @Result = Salary
    FROM
    (
        SELECT DISTINCT Salary,
               DENSE_RANK() OVER (ORDER BY Salary DESC) AS RankNo
        FROM Employee
    ) AS T
    WHERE RankNo = @N;

    RETURN @Result;
END;