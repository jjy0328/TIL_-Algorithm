number = input()
result = 0

for n in number:
    # 0으로 시작하는 경우에도 똑같이 해주어야 함.
    if int(n) <= 1 or result <= 1:
        result += int(n)
    else:
        result *= int(n)

print(result)
