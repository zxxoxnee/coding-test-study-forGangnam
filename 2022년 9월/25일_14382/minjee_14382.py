# 14382
t = int(input())

for i in range(t):
    check = {}
    n = int(input())
    now = n
    if n == 0:
        print("Case #", i, ": INSOMNIA")
    else:
        count = 1
        while True:
            temp = str(now)
            for j in temp:
                if int(j) not in check:
                    check[j] = 1
                else:
                    continue
            if sum(check.values()) == 10:
                print("Case #",i, ": ",now)
                break
            count += 1
            now = n * count
