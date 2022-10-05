def solution(s):

    # 공백을 구분으로 문자 구분 후, int로 형변환하여 list화
    ss = list(map(int, s.split(' ')))

    # 최댓값과 최솟값 return
    return str(min(ss))+' '+str(max(ss))