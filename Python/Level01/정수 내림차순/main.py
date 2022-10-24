def solution(n):
    # 큰수부터 나열
    str_n = sorted(str(n), reverse=True)
    # join : 배열의 모든 요소를 합쳐 하나의 문자열로 변환
    answer = ''.join(str_n)
    # 결과값이 str 타입이기에 int 타입으로 변환
    return int(answer)