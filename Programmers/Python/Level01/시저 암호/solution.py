# collections : deque의 rotate 이용
# string : 알파벳 쉽게 정렬

import collections
import string

def solution(s, n):
    
    lower = collections.deque([i for i in string.ascii_lowercase])
    upper = collections.deque([i for i in string.ascii_uppercase])
    answer = ''
    
    # 해당 알파벳이 있는 index를 구한 후, n을 더한만큼 왼쪽으로 회전
    # " "는 바로 answer에 더해주기
    for i in s:
        if i in upper:
            idx = upper.index(i)
            upper.rotate(-(n+idx))
            answer += upper[0]
        elif i in lower:
            idx = lower.index(i)
            lower.rotate(-(n+idx))
            answer += lower[0]
        elif i == ' ':
            answer += ' '
            
    return answer