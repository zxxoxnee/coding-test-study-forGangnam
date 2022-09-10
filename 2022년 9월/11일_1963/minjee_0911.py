# https://www.acmicpc.net/problem/1963
from collections import deque
import sys
# 에라토스테네의 체 -> 소수 판별
array = [True] * 10000

for x in range(2, 100):
    if array[x]:
        y = 2
        for y in range(x*2, 10000, x):
            array[y] = False

def solve(a, b):
    queue = deque()
    queue.append((a, 0)) # (현재 비밀번호, count)
    visited = [False] * 10000 # 1000 ~ 9999 표시
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
                temp = int(str_num[:i] + str(j) + str_num[i+1:])
                if visited[temp] == False and array[temp] == True:
                    visited[temp] = True
                    queue.append((temp, count+1))

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = solve(a, b)
    if result != None:
        print(result)
    else:
        print("Impossible")

# 이런 경우 왜 bfs를 쓸까 ?