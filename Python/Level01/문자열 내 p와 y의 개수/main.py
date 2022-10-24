def solution(s):
    s1 = s.lower()
    tmp1=[]
    tmp2=[]
    for i in s1:
        if i == 'y':
            tmp1.append(i)
        elif i == 'p':
            tmp2.append(i)
    
    if len(tmp1) == len(tmp2):
        answer = True
    else:
        answer = False
        
    return answer