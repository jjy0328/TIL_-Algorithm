def solution(s, n):
    s = list(s)

    # chr() : 아스키 코드 -> 문자
    # ord() : 문자 -> 아스키 코드
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)