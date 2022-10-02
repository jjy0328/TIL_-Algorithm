lst = []

def solution(arr, divisor):
    
    for i in arr:
        if i % divisor == 0:
            lst.append(i)

    if len(lst) == 0:
        answer = [-1]
    else:
        lst.sort()
        answer = lst
            
    return answer

def solution(arr, divisor): 
    
    # 앞의 조건이 거짓일 때, [-1] 출력
    return sorted([n for n in arr if n%divisor == 0]) or [-1]