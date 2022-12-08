# 처음 시도한 코드
def solution(arr):
    
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        answer = sorted(arr, reverse = True)[:-1]
            
    return answer


# 런타임 에러

def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    else:
        return remove(min(arr))
            


# 정답

def solution(arr):
    
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    
    else:
        return [-1]