def solution(absolutes, signs):
    answer = 0
    
    # index를 기준으로 for문을 잘라 붙여주는 함수 zip 이용하여
    # true일 시 answer에서 더해주고
    # falsw일 시 answer에서 빼주기
    for num, sign in zip(absolutes, signs):
        if sign == True:
            answer += num
        elif sign == False:
            answer -= num
            
    return answer