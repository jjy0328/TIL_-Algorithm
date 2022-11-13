def solution(n):
    answer = 0
    # n을 이진수로 변환 후 count 쉽게 str변환
    str_n = str(bin(n))
    
    # n은 1,000,000 이하의 자연수이기에 범위 아래와 같이 설정
    for i in range(n+1, 1000000):
        # i도 똑같이 이진수 변환 후 str 변환
        str_i = str(bin(i))
        # 1을 count해서 같으면 answer로 변환 후 for문 빠져나오기
        if str_n.count('1') == str_i.count('1'):
            answer = i
            break
            
    return answer