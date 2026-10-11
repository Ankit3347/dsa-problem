# Write your MySQL query statement below
select
e.name Employee
from employee e
join employee m
on e.managerId=m.Id
where m.salary<e.salary
