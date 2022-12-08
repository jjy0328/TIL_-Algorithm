def solution(price, money, count):
    answer = 0
    fee = 0
    
    for i in range(1, count+1):
        fee += (price * i)
        
    answer = fee - money
    
    if answer > 0:
        return answer
    
    else:
        return 0