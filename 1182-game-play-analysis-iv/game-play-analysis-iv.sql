# Write your MySQL query statement below
select
    round(
        avg(case when a2.player_id is not null then 1 else 0 end)
    , 2) as fraction
from
    activity a1
    left join
    activity a2
    on
        a1.player_id = a2.player_id
        and
        a1.event_date = date_sub(a2.event_date, interval 1 day)
where 
    (a1.player_id, a1.event_date) in (
        select 
            player_id, 
            min(event_date)
        from 
            activity
        group by 
            player_id
    )