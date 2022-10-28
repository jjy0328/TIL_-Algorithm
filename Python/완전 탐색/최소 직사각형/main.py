# 명함 하나의 가로, 세로 중 더 긴 것을 w 리스트에, 짧은 것을 h 리스트에 넣고
# 각 리스트에서 max값을 곱하면 되는 문제

def solution(sizes):
    
    w = []
    h = []
    
    for i,j in sizes:
        if i > j:
            w.append(i)
            h.append(j)
            
        else:
            w.append(j)
            h.append(i)
            
    return max(w) * max(h)