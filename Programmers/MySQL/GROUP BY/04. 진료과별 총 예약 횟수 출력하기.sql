-- MySQL에서 유형별로 갯수를 가져오고 싶은데, 단순히 COUNT 함수로 데이터를 조회하면 전체 갯수만을 가져옴
-- 이렇게 유형별로 갯수를 알고 싶을 때는 컬럼에 데이터를 그룹화 할 수 있는 GROUP BY를 사용하는 것임

SELECT MCDP_CD AS 진료과코드, COUNT(APNT_YMD) AS 5월예약건수
 FROM APPOINTMENT
 WHERE APNT_YMD LIKE '2022-05%'
 GROUP BY MCDP_CD
 ORDER BY 2,1;