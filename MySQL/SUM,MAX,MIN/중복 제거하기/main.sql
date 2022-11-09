--  SQL 중복 제거는 distinct 쓸 것
SELECT COUNT(DISTINCT(NAME)) AS count 
    FROM ANIMAL_INS
    WHERE NAME != 'NULL'