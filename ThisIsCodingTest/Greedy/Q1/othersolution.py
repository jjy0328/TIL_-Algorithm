# N, K를 고백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어진 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    # n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

    # 남은 수에 대해 1씩 빼기
    print(result)