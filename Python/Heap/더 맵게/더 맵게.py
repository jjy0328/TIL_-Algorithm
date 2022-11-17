import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) != 1:
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        cnt += 1
    
    if scoville[0] < K:
        return -1
    
    else:
        return cnt  