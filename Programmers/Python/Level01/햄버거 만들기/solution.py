#### del을 활용하여 [1,2,3,1]을 아예 지워버리는 방법

def solution(ingredient):
    ham = []
    answer = 0
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1, 2, 3, 1]:
            answer += 1
            del ham[-4:]
    return answer


#### pop을 4번 반복하여 [1,2,3,1]을 하나씩 없애는 방법

def solution(ingredient):
    ham = []
    answer = 0
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                ham.pop()
    return answer