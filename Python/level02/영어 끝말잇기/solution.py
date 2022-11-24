def solution(n, words):
    answer = [0,0]
    gamers = 2   # 첫 번째 사람이 걸릴 일은 없기 때문
    turn = 1     # 첫 번째 턴이 끝나기 전에 누군가 걸릴 가능성도 있음
    pre_word = [words[0]]  # 끝말잇기에 등장한 단어들 리스트
    last_word = words[0]   # 이전 단어와 비교할 것들
    
    for word in words[1:]:
        # 이전 나온 단어와 비교 + 끝말잇기 여부 비교
        if last_word[-1] != word[0] or word in pre_word: 
            answer = [gamers, turn]
            break
            
        pre_word.append(word)  # 등장한 단어 추가
        last_word = word       # 이전 단어 변경
        gamers += 1            # 순서 변경
        
        if gamers > n:  
            gamers = 1   # 한 턴이 끝나면 처음 사람도 걸릴 가능성이 있기에 gamers 1로 초기화
            turn += 1
    
    return answer