# 문제 

## 처음 제출한 답안 : 테스트케이스 6번만 통과하지 못함
def solution(N):
    count = 1
    while N > 1:
        count += N % 2
        N //= 2
    return count

## 정답 답안
def solution(N):
    count = 1
    while N > 1:
        count += N % 2
        N //= 2 
    return count

#### 숫자 N은 1 이상인 경우만 해당됨.
#### 1인 경우엔 count는 그냥 1이기 때문