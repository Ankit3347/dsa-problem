/* Write your T-SQL query statement below */
with ClassName as(
    select 
    class,
    count(student) as TotalStudent
    from courses
    group by class
)

select class
from ClassName
where TotalStudent>=5