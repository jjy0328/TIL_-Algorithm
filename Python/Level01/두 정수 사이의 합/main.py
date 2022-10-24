def solution(a,b):
    
    # a가 b보다 작은 경우, a부터 시작하는 리스트 만들기
    if a < b :
        answer = [i for i in range(a,b+1)]
    # a가 b보다 b 경우, a부터 시작하는 리스트 만들기
    else :
        answer = [i for i in range(b,a+1)]
        
    return sum(answer)