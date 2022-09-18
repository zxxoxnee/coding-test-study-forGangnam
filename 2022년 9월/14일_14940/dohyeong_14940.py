
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 원래 0인 땅 때문에 못가는 경우는 기본 그래프 -1로 넣어서 해결
res = [[-1] * m for _ in range(n)]
# 목표 지점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x,y = i,j
            # 시작 지점은 0
            res[i][j] = 0
        elif graph[i][j] == 0:
            res[i][j] = 0

# print(res)

def bfs(graph, res, x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        # print((x,y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    res[nx][ny] = res[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
                # 원래 0인부분에서는 방문처리만
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
    return res

# print(bfs(graph, res, x, y))
bfs(graph, res, x, y)

for i in range(n):
    print(" ".join(map(str,res[i])))

