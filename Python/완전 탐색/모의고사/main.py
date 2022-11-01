def solution(answers):
    
    # 학생이 찍은 답 리스트로 만들기
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # answer  = return할 값
    # cnt = 학생 별로 정답을 맞춘 수
    answer = []
    cnt = [0,0,0]
    
    # std1[i%5]은 student1의 길이로 나눈 것의 나머지 값
    # answers의 0~len(answer)까지의 인덱스를 반복 가능
    # 맞은 만큼 cnt 리스트에 + 1을 해주어 맞은 갯수 count
    for i in range(len(answers)) :
        if answers[i] == std1[i%5] :
            cnt[0] += 1
        if answers[i] == std2[i%8] :
            cnt[1] += 1
        if answers[i] == std3[i%10] :
            cnt[2] += 1
    
    ####### 다른 사람 코드 참고한 부분 #########
    # enumerate를 하는 이유 : 
    # 마지막에 max 값의 index를 알아야 학생의 번호를 알 수 있기 때문

    for idx, num in enumerate(cnt) :
        if num == max(cnt) :
            answer.append(idx +1)
    
    return answer