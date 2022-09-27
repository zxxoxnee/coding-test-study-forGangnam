# 1717 백준

n, m = map(int, input().split())
array = [[i] for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        # 합치기
        idx = -1
        for i in range(n+1):
            if a in array[i]:
                idx = i
            if b in array[i]:
                array[i].remove(b)
        array[idx].append(b)

    else: # 연산 확인하기
        flag = False
        for i in range(n+1):
            if a in array[i] and b in array[i]:
                flag = True
        if flag:
            print("YES")
        else:
            print("NO")
