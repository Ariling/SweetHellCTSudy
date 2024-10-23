-- 코드를 작성해주세요
SELECT e.ID, sub.FISH_NAME, sub.LENGTH
FROM FISH_INFO e
JOIN (
select e2.FISH_NAME as FISH_NAME , MAX(e1.LENGTH) as LENGTH, e2.FISH_TYPE as type from FISH_INFO e1, FISH_NAME_INFO e2 where e1.FISH_TYPE = e2.FISH_TYPE group by e2.FISH_NAME, e2.FISH_TYPE
) sub ON (e.LENGTH = sub.LENGTH and e.FISH_TYPE = sub.type);