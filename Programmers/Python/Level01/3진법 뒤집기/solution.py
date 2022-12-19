def solution(n):
    answer = ''
    
    while n > 0:
        # 3진법 변환 후 반전된 상태로 저장하기
        answer += str(n%3)
        n = n//3
    
    # 3진법을 10진법으로 다시 변환하는 법
    return int(answer,3)