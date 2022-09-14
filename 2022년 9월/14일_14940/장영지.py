import sys
from collections import deque


n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n) :
  a = list(map(int, sys.stdin.readline().split()))
  graph.append(a)

result = [[-1 for _ in range(m)] for _ in range(n)] 
visit = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 
def dfs(x,y) :
  # deque 생성
  queue = deque()
  queue.append((x, y, 0))

  while queue:
    x, y, cnt = queue.popleft()
    if visit[x][y] : 
      continue
    visit[x][y] = True
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1 and not visit[nx][ny]:
        result[nx][ny] = cnt + 1
        queue.append((nx, ny,cnt +1))

for i in range(n) :
  for j in range(m) :
    if graph[i][j] == 0 :
      result[i][j] = 0

for i in range(n) :
  for j in range(m) :
    if graph[i][j] == 2 :
      result[i][j] = 0
      dfs(i,j)
      break


for i in result :
  print(*i)

