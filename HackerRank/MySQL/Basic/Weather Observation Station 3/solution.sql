select distinct (CITY) from STATION
where mod(ID,2) = 0;

/* MOD(a,b) : a를 b로 나눈 나머지값 반환
   xclude duplicates : 같은 값을 제외하기 위해 DISTINCT 이용하기 */