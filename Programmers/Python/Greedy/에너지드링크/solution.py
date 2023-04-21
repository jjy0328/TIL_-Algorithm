N = int(input())
drink = list(map(int, input().split()))
drink.sort()

# 음료의 양을 최대로 하기 위해선 오름차순으로 정렬 후
# 가장 많은 양의 음료에서 나머지 반으로 나눈 후 더하기
answer = drink[-1]
for i in range(N-1):
    answer += drink[i] / 2

print(answer)
