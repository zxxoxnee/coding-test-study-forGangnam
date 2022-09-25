# 14382
t = int(input())

for i in range(t):
    check = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    n = int(input())
    temp = str(n)
    for j in temp:
        check[int(j)] += 1

    # 확인하기


    print("Case #",i,":")