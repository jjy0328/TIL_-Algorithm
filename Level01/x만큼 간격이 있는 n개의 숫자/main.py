def solution(x,n):
    answer = []
    
    # 0이 포함되지 않고, n 자신을 포함해야함
    for i in range(1,n+1):
        answer.append(i*x)
        
    return answer