def solution(x):
    
    # 각 자릿수를 구하기 위해 string 타입으로 변환
    str_x = str(x)
    
    # add_num 선언
    add_num = 0
    
    # 각 자릿수를 int로 변환한 후, add_num에 더하기
    for i in str_x:
        add_num += int(i)

    # x로 나눈 값의 나머지가 0인 경우, true
    # 0이 아니면 false
    if x % add_num == 0:
        answer = True
    else:
        answer = False
        
    return answer



 
def solution(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0