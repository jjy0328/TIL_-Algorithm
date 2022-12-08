def solution(a, b):
    answer = 0
    
    # zip 함수를 이용하여 각 원소를 곱한 후
    # answer에 더해주기
    for i,j in zip(a,b):
        answer += i*j
        
    return answer