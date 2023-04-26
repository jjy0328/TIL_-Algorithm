# 재귀함수를 사용했으나 런타임 에러가 남
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution(n - 1) + solution(n - 2)
    

# 다른 사람의 풀이
def solution(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1])%1234567
    return dp[n]
#시간복잡도 = O(n), 공간복잡도 = O(n)