from collections import deque

n = int(input())
data = list(map(int, input().split()))
data.sort()

adventure = [] # 모험을 떠나는 그룹
answer = 0 # 정답

for i in data:
    adventure.append(i)
    data.pop()
    # 공포도 가장 큰 값보다 모인 사람의 수가 많으면 모험을 떠나기
    if len(adventure) >= max(adventure):
        answer += 1
        # adventure 초기화
        adventure = []
    
print(answer)
    