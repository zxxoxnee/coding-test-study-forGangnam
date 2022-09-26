# 14382
t = int(input())

for i in range(t):
    check = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    n = int(input())
    if n == 0:
        print("Case #", i, ": INSOMNIA")
    else:
        count = 1
        while True:
            temp = str(n)
            for j in temp:
                check[int(j)] = 1
            total = 0
            for k in check.values():
                if k != 0:
                    total += 1
            if total == 10:
                print("Case #", i, ": ",n)
                break
            n *= count

    # 확인하기


