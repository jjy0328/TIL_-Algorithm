# 재귀함수를 사용했으나 런타임 에러가 남
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution(n - 1) + solution(n - 2)