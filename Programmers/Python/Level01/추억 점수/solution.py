def solution(name, yearning, photo):
    answer = []
    missing = dict()

    # dictionary로 이름과 yearing 미리 짝지어넣기
    for i in range(len(name)):
        missing[name[i]] = yearning[i]
    
    for kids in photo:
        cnt = 0
        for kid in kids:
            if kid in name:
                cnt += missing[kid]
        answer.append(cnt)
    return answer