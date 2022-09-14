# 틀린 코드

from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

res = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            res[i][j] == 0
        if graph[i][j] == 2:
            res[i][j] == 0
            start = (i,j)

visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 목적지를 기준으로 bfs 순회
def bfs(start, visited, graph, res):
    q = deque(start)
    visited[start[0]][start[1]] = True
    while q:
        x,y = start[0], start[1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx,ny))
                    visited[nx][ny] = True
                # 주의
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
bfs(start,visited, graph, res)
print(res)