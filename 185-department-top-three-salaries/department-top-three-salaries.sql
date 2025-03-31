# Write your MySQL query statement below
SELECT Department, employee, salary FROM (
    SELECT d.name AS Department
        , e.name AS employee
        , e.salary
        , DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS drk
    FROM Employee e JOIN Department d ON e.DepartmentId= d.Id
) t WHERE t.drk <= 3