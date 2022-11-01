###### 효율성 측면이 아쉬움 #######

def solution(arr):
    
    # 맨 처음 element 추가하고 시작
    answer = [arr[0]]
    
    # arr 리스트의 1번 element와 0번 element를 비교하여 다르면 리스트에 담는 식
    for idx in range(1,len(arr)):
        if arr[idx] != arr[idx-1]:
            answer.append(arr[idx])
            
    return answer



#### 다른 사람 코드 (원래 구현하고자했던 코드)
# a라는 빈 리스트를 만들어 놓고, a의 마지막 요소와 일치하면 continue, 그렇지 않으면 append
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a