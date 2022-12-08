def solution(n, m):
    min = 0
    max = 0
    answer = []
        
    for i in range(m, 0, -1):
        if n % i == 0 and m % i == 0:
            min = i
            break
            
    for j in range(n, (n * m) + 1):
        if j % n == 0 and j % m == 0:
            max = j
            break
        
    return [min, max]