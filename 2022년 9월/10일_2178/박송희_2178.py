import sys
from collections import deque

n, m = map(int, input().split())
board = []

for i in range(n) :
    line = input()
    temp = []
    for j in line : 
        temp.append(int(j))
    board.append(temp)

distanced = [[0] * m for _ in range(n)]

def BFS(startX, startY) :
    dx = [-1, 0, 1, 0] 
    dy = [0, 1, 0, -1]
    dq = deque()

    dq.append((startX, startY))
    board[startX][startY] = 0
    distanced[startX][startY] = 1

    while dq :
        nowX, nowY = dq.popleft()

        for d in range(4) :
            nextX = nowX + dx[d]
            nextY = nowY + dy[d]

            if 0 <= nextX < n and 0 <= nextY < m and board[nextX][nextY] == 1 :
                dq.append((nextX, nextY))
                board[nextX][nextY] = 0
                distanced[nextX][nextY] = distanced[nowX][nowY] + 1

    print(distanced[n-1][m-1])



BFS(0, 0)