# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016 from insurance n
where (lat,lon) not in (select lat,lon from insurance i where n.pid!=i.pid)
and tiv_2015 in (select tiv_2015 from insurance i where n.pid!=i.pid)