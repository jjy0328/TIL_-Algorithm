def solution(s):
    
    answer = []
    tmp = s.split(' ')

    for words in tmp:
        word = []
        for i in range(len(words)):
            if i % 2 == 0:
                word.append(words[i].upper())
            elif i % 2 != 0:
                word.append(words[i].lower())
        answer.append(''.join(word))
            
    return ' '.join(answer)