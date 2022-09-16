# 14502 연구소
from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
array = []

for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바이러스 퍼뜨리는 함수
def virus(x, y):
    temp = copy.deepcopy(array)
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))
    return temp

