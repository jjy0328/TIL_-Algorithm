def solution(strings, n):
    # 아스키코드 따로 빼둘 리스트
    # n번째 아스키코드가 똑같을 상황을 대비하여 strings 미리 정렬해두기
    ASCII = []
    answer = []
    strings.sort()
    
    # 각 단어의 n번째 아스키코드가 겹치면 똑같은 단어가 중복되어 들어가기 때문에 중복 방지
    for i in strings:
        if ord(i[n]) not in ASCII:
            ASCII.append(ord(i[n]))
    
    # sort를 마지막에 해주기
    ASCII.sort()
    
    # 숫자에 맞는 아스키코드 반환 후, 각 단어의 n번째와 같으면 append
    for j in ASCII:
        for k in strings:
            if chr(j) == k[n]:
                answer.append(k)
                
    return answer