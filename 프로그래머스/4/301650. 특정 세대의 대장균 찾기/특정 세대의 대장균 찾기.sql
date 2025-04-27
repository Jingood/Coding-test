# select GP.ID
# from ECOLI_DATA C join ECOLI_DATA P on C.ID = P.PARENT_ID inner join ECOLI_DATA GP on P.ID = GP.PARENT_ID
# where C.PARENT_ID is NULL
# order by GP.ID

# select GP.ID
# from ECOLI_DATA as GP
# where GP.PARENT_ID in
# (
# select P.ID
# from ECOLI_DATA as P
# where P.PARENT_ID in
#     (
#     select C.ID
#     from ECOLI_DATA as C
#     where C.PARENT_ID is NULL
#     )
# )
# order by GP.ID

select GP.ID
from ECOLI_DATA as GP
where exists (
    select P.ID
    from ECOLI_DATA as P
    where GP.PARENT_ID = P.ID
        and exists (
            select C.ID
            from ECOLI_DATA as C
            where P.PARENT_ID = C.ID
            and C.PARENT_ID is NULL
        )
)
order by GP.ID