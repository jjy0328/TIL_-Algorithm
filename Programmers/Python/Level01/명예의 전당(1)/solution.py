def solution(k, score):
    answer = []
    glory = []
    
    for i in range(len(score)):
        # k번째 미만에 있는 요소의 경우 무조건 glory에 append
        # glory에서 가장 작은 수 answer에 append
        if i < k:
            glory.append(score[i])
            glory.sort()
            answer.append(glory[0])
            
        # k번째 이상에 있는 요소의 경우 glory의 0번째 수보다 큰 경우 answer에 append
        # 그렇지 않을 경우 glory의 0번째 수 answer에 append
        elif i >= k:
            if score[i] > glory[0]:
                del glory[0]
                glory.append(score[i])
                glory.sort()
                answer.append(glory[0])
            else:
                answer.append(glory[0])
                
            
    return answer