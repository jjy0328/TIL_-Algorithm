-- 처음 작성한 코드 (오류)

SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE, PRODUCT_NAME
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
    HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
    ORDER BY MAX_PRICE DESC;

-- 위의 코드로 코드를 작성했을 시, 카테고리 별로 분류한 후 product_id가 가장 낮은 순으로 정렬
-- 그 후, price만 카테고리 별로 가장 높은 가격을 불러옴
-- 서브쿼리를 써서 카테고리 별로 가격이 가장 높은 품목을 불러오고
-- 가격 순으로 정렬해야 하는 문제



-- 올바른 코드 (@starryboram 님이 알려주셨습니다.)

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
    FROM FOOD_PRODUCT
    WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
    AND CATEGORY IN ('과자', '국', '김치', '식용유')
    ORDER BY MAX_PRICE DESC;

-- FOOD_PRODUCT 테이블 : FROM FOOD_PRODUCT
-- 식품분류별로 가격이 제일 비싼 식품 조회: SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
-- 분류, 가격, 이름을 조회: SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력: AND CATEGORY IN ('과자', '국', '김치', '식용유')
-- 식품 가격을 기준으로 내림차순 정렬: ORDER BY MAX_PRICE DESC
-- ※ 각 행별로 최대 가격을 봐야함 => WHERE 구문에 서브쿼리 이용해서 집어넣기