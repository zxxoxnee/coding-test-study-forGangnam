import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph= []
for _ in range(n) :
  a = list(map(int,sys.stdin.readline().strip()))
  graph.append(a)

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]


x,y = 0,0
count = n*m
queue = deque()
queue.append([x,y])

while queue :
  x,y = queue.popleft()

  for i in range(4) :
    xx = x +dx[i]
    yy = y + dy[i]

    if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 1:
      queue.append([xx,yy])
      graph[xx][yy] = graph[x][y] + 1

print(graph[n-1][m-1])