def solution(left, right):
    answer = 0
    numbers = range(left, right+1)
    
    for number in numbers:
        divisor = []
        for num in range(1,number+1):
            if number % num == 0:
                divisor.append(num)
    
        if len(divisor) % 2 == 0:
            answer += number
        else:
            answer -= number
            
    return answer