-- 코드를 작성해주세요
SELECT e1.ID as ID, (select IFNULL(count(parent_id), 0) from ECOLI_DATA e2 where e2.PARENT_ID = e1.ID) as CHILD_COUNT
from ECOLI_DATA e1 order by ID;