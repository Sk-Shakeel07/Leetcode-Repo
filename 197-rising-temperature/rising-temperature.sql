# Write your MySQL query statement below
SELECT 
	tday.id
FROM weather tday
JOIN weather yday
ON tday.recordDate = DATE_ADD(yday.recordDate, INTERVAL 1 DAY)
WHERE tday.temperature > yday.temperature;