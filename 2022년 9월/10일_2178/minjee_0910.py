# https://www.acmicpc.net/problem/2178
# 미로 탐색
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dist = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 1 # 방문
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist[n-1][m-1]

print(bfs(0, 0))