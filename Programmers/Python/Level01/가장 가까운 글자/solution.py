def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[0:i]:
            answer.append(i - s[0:i].rindex(s[i]))
        else:
            answer.append(-1)
    return answer


####### 05/17일 풀이 : dictionary를 활용함 ###########
def solution(s):
    answer = []
    dict_s = dict()

    for i in range(len(s)):
        if s[i] not in dict_s:
            answer.append(-1)
        else:
            answer.append(i - dict_s[s[i]])
        # 해당 요소가 가장 마지막에 나온 때로 업데이트를 해주어야 함
        dict_s[s[i]] = i
        
    return answer