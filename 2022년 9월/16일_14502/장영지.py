from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n) :
  a = list(map(int, sys.stdin.readline().split()))
  graph.append(a)

# 모든 경우를 확인,,,,,????!! 
dx = []
dy = []

def virus(virus,x,y) :  # 바이러스 퍼진 그래프
  que = deque()
  que.append(x,y)

  while que :
    a,b = que.pop()

    for i in range(4) :
      xx = a + dx[i]
      yy = b + dy[i]

      if 0 <= xx <= n and 0 <= yy <= m and virus[xx][yy] == 0 :
        virus[xx][yy] = 2
        que.append(xx,yy)
  
  return virus

def safe(safezone,x,y): # 안전지대
  que = deque()
  que.append(x,y)
  count = 0
  while que :
    a,b = que.pop()

    for i in range(4) :
      xx = a + dx[i]
      yy = b + dy[i]

      if 0 <= xx <= n and 0 <= yy <= m and safezone[xx][yy] == 0 :
        safezone[xx][yy] = 1
        count += 1
        que.append(xx,yy)

  return count

