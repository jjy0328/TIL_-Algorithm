def solution(s):
    
    if len(s) % 2 == 0:
        idx = len(s)//2 - 1
        idx2 = len(s)//2 + 1
        answer = s[idx:idx2]
        
    else:
        idx = len(s)//2
        answer = s[idx]
        
    return answer