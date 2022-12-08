import math

def solution(n):
    # x의 제곱이 n이 되는 정수를 구하는 함수 sqrt
    x = math.sqrt(n)
    if x != int(x):
        anwser = -1
    else:
        # 제곱근을 구하는 함수 pow
        anwser = math.pow(x+1, 2)
    return anwser