### 재귀함수 사용 시 런타임 에러가 뜸
def solution(n):
    
    # if문을 사용하여 F(0) = 0, F(1) = 1 값 리턴
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 재귀함수 사용하기
    else:
        return solution(n - 1) + solution(n - 2)
    

### 다른 사람('라떼는 말이야'님)의 풀이 참고

def solution(n):
    # 문제에서 주어진 F(0) = 0, F(1) = 1는 미리 리스트에 넣어두기
    lst = [0, 1]
    # 2 이상부터 문제의 공식 대입 후 리스트에 넣기
    # 피보나치 수를 1234567으로 나눈 나머지 값을 원하기에 미리 나눠줌
    for i in range(2, n + 1):
        fib.append((lst[i-2] + lst[i-1]) % 1234567)
    
    return fib[-1]