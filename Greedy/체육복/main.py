# 예제 1번만 맞았던 코드
# 체육복을 도난당하지 않았던 학생 중, 여벌을 가진 학생을 고려하지 않았음

def solution(n, lost, reserve):
    for i in reserve:
        for j in lost:
            if j == (i+1):
                reserve.append(j)
    return len(reserve)



# 맞춘 코드
def solution(n, lost, reserve):
    
    # 각 리스트 중복 제거
    # 여벌이 있는 학생들도 도난 당했을 수도 있기 때문에 set 사용해주기
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    # reserve set의 각 요소에서
    # reserve set +1 이 존재하는 경우 lost_set에서 지워주기
    # resreve -1이 존재하는 경우, lost_set에서 지워주기
    for i in reserve_set: 
        if i-1 in lost_set: 
            lost_set.remove(i-1) 
        elif j+1 in lost_set: 
            lost_set.remove(j+1) 
    
    # n에서 for문을 돌리고 남은 set의 길이만큼 빼주기
    return n-len(lost_set)