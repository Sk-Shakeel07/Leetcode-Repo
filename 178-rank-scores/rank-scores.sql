# Write your MySQL query statement below
with scores_cte as (
    select id, score,
    dense_rank() over (order by score desc) as "rank"
    from Scores
)

select score, dense_rank() over (order by score desc) as "rank" 
from scores_cte