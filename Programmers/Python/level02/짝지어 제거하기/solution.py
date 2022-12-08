##### stack을 이용하면 매우 간단한 문제 ######

def solution(s):
    answer = 0
    s = list(s)
    tmp = []
    
    # tmp라는 빈 리스트를 두고
    # 루프를 도는 동안 길이가 0이면 해당 element 추가하기
    # tmp의 마지막 번째 element와 해당 loop의 elment가 같으면
    # pop을 이용하여 삭제
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
        elif i == tmp[-1]:
            tmp.pop()
        else:
            tmp.append(i)

    # for문이 완전히 끝난 후, tmp 리스트의 길이가 0이면 1 return
    if len(tmp) == 0:
        answer = 1

    return answer