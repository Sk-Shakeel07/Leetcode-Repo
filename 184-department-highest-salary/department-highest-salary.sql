# Write your MySQL query statement below
select Department,e.name as Employee,e.salary as Salary 
from employee e,
(
    select d.id department_id,d.name as Department,max(e.salary) as max 
    from department d left join employee e 
    on  d.id=e.departmentId 
    group by d.id
) as MaxSalaries 
where e.departmentId=department_id and e.salary = max;