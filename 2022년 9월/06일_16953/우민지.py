# 16953 우민지

a, b = map(int, input().split())
count = 1
while True:
    if b == a: # A->B 가능한 경우
        break
    elif (b < a) or (b%10 != 1 and b%2 != 0): # A->B 불가능한 경우 예외처리
        count = -1
        break
    else:
        if b%10==1:
            b = b//10
            count += 1
        else:
            b = b//2
            count += 1
print(count)
