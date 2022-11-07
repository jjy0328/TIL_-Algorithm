a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print('*',end='')
    print(end='\n')
    

###### 참고한 다른 사람 코드 ######
print(("*" * a + "\n") * b)