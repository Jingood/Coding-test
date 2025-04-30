with recursive GENERATIONS as (
    select
        ID,
        PARENT_ID,
        1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select
        CHILD.ID,
        CHILD.PARENT_ID,
        PARENT.GENERATION + 1 as GENERATION
    from ECOLI_DATA as CHILD join generations as PARENT on CHILD.PARENT_ID = PARENT.ID
)

select
    count(*) as COUNT,
    G.GENERATION as GENERATION
from GENERATIONS as G
where not exists (
    select GENERATION
    from ECOLI_DATA as e2
    where e2.PARENT_ID = G.ID
)
group by G.GENERATION
order by G.GENERATION