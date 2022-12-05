def solution(brown, yellow):
    answer = []
    sum_ = brown+yellow
    
    for w in range(1, sum_):
        if sum_ % w == 0:
            h = sum_ // w
            if w < h:
                w, h = h, w
            if yellow == sum_ - (2 * w + 2 * h - 4):
                return  [w, h]