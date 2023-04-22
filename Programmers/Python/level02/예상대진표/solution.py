def solution(n,a,b): 
	answer = 0
	while a != b: 
		answer += 1
		# 2로 나누었을 때 3이든 4이든 값이 같도록 맞춰줌
		a = (a+1)//2
		b = (b+1)//2
	return answer