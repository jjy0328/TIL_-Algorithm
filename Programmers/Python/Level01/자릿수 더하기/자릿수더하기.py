def solution(n):
    # map(function, iterable)
    # 자동으로 리스트를 map 함수에 적용하여 map 객체 반환
    x = list(map(int, str(n)))
    answer = sum(x)
    return answer