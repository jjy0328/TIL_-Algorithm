def solution(numbers):
    
    num = range(1,10)
    answer = sum(range(1,10))
    
    # num에서 없는 숫자를 더하는 것보다,
    # num과 numbers에서 일치하는 숫자를
    # 1 ~ 10의 총합에서 빼는 것이 더 빠를 것이라 판단함
    
    for number in numbers:
        if number in num:
            answer -= number
            
    return answer