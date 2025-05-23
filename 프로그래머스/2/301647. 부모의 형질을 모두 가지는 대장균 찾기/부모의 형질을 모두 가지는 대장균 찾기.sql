select C.ID, C.GENOTYPE, P.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA C join ECOLI_DATA P on C.PARENT_ID = P.ID
where (C.GENOTYPE & P.GENOTYPE = P.GENOTYPE)
order by C.ID