n, m = map(int, input().split())

answer = 0

while m > n:
    if m % 2 == 0:
        m = int(m / 2)
        answer += 1
    elif int(list(str(m))[-1]) == 1:
        m = int("".join(list(str(m))[:-1]))
        answer += 1
    else:
        break

if m == n:
    print(answer+1)
else:
    print(-1)
