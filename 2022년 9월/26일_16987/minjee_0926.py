# https://www.acmicpc.net/problem/16987
n = int(input())
array = [] # 계란 배열
check = [False]*n  # 깨지지 않으면 false, 깨지면 true

for _ in range(n):
    s, w = map(int, input().split())
    array.append([s, w])

for i in range(n):
    if not check[i]:
        hand = array[i] # 손에 드는 계란
        for j in range(i + 1, n):
            if not check[j]:
                h_s, h_w = hand[0], hand[1]
                e_s, e_w = array[j][0], array[j][1]
                if h_s <= e_w:
                    # 손에 든 계란 깨짐
                    check[i] = True
                if e_s <= h_w:
                    check[j] = True
count = 0
for i in check:
    if i:
        count += 1

print(count)