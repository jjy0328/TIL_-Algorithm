def solution(d, budget):
    # 최대한 많은 물품을 지원해주기 위해선 작은 수부터 정렬하는게 유리함
    d.sort()
    answer = 0
    # 예산에서 오름차순으로 정렬한 리스트의 요소들 차례로 빼주기
    # 한 번 뺄 때마다 answer에 1씩 더해주기
    # 음수가 되면 for문 break
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer