def solution(s):
    
    words={"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for key in words.keys():
        if key in s:
            s = s.replace(key, words[key])
    
    return int(s)