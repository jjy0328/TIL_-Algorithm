def solution(phone_number):
    
    # 가릴 문자열을 replace
    answer = phone_number.replace(phone_number[:-4], 
                                  '*'*len(phone_number[:-4]))
    return answer