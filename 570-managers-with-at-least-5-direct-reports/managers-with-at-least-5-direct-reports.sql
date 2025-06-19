# Write your MySQL query statement below
select a.name 
from Employee as a 
Join Employee as b on a.id = b.id
where a.id in (select managerId from Employee group by managerId having count(managerId)>=5  );