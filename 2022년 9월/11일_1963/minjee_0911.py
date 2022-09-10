# https://www.acmicpc.net/problem/1963
from collections import deque
# 에라스토스의 체 -> 소수 판별
array = [True] * (10000)
for i in range(10000):
    if array[i]:
        j = 2
        while i*j < 10000:
            array[i*j] = False
            j += 1

def solve(a, b):
    queue = deque()
    queue.append((a, 0)) # (현재 비밀번호, count)
    visited = [False] * 10001 # 1000 ~ 9999 표시
    visited[a] = True
    while queue:
        num, count = queue.popleft()
        if num == b:
            return count # result
        if num < 1000: # 네자리수 이하 안됨
            continue
        # 한자리씩 바꿔보면서 소수이면서 not visited한 것 큐에 append
        str_num = str(num)
        for i in range(4):
            for j in range(10): # 0 ~ 9
                temp = int(str_num[:i] + str(j) + str_num[i:])
                if visited[temp] == False and array[temp] == True:
                    visited[temp] = True
                    queue.append((temp, count+1))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = solve(a, b)
    if result == None:
        print("Impossible")
    else:
        print(result)

