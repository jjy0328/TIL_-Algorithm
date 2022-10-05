def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize : 첫 문자가 알파벳일 경우 대문자로 만든 후
        # 두번째 문자부터는 소문자로 만들어줌
        # 첫 문자가 알파벳이 아닐 시, 그대로 return
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

# title 함수와 capital 함수의 차이점
# a = 'a1b2n3'일 때,
# a.capitalize() -> output: 'A1b2n3'
# a.title() -> output : 'A1B2N3'
# title은 알파벳 외의 문자를 기준으로 대문자로 만들고,
# capitalize는 단어의 첫 글자가 알파벳일시 대문자로 만들어줌