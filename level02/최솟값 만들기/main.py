def solution(A,B):
    
    # 핵심이 되는 공식 : answer = answer + (A[i] * B[i])
    # 위의 공식으로 최솟값을 만들기 위해 
    # a는 오름차순, b는 내림차순으로 정렬
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer = 0

    for i in range(len(A)):
        answer = answer + (A[i] * B[i])

    return answer