def solution(n):
    tmp = []
    for i in range(n+1)[1:]:
      if n % i == 0:
        tmp.append(i)
    answer = sum(tmp)
    return answer