-- 코드를 입력하세요
SELECT AI.ANIMAL_ID, AI.NAME
    FROM ANIMAL_INS AS AI
    JOIN ANIMAL_OUTS AS AO
        ON AI.ANIMAL_ID = AO.ANIMAL_ID
    WHERE AI.DATETIME > AO.DATETIME
    ORDER BY AI.DATETIME ASC;


-- 날짜도 연산가능!

-- SELECT CURRENT_DATE + INTERVAL 1 DAY
-- 위의 식처럼 interval을 이용하여 년,월,일 더하기도 가능함

-- SELECT DATEDIFF('2022-12-25', '2022-11-16');
-- 위의 식처럼 datediff를 활용하여 날짜끼리 뺄 수도 있음