#https://www.acmicpc.net/problem/14940


from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
board = []
dq = deque([])
visited = [[False]*m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))

    # 목표지점 찾기
    for j in range(m):
        if row[j] == 2:
            dq.append((i, j))
            visited[i][j] = True
            row[j] = 0
    board.append(row)

# BFS 탐색
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우
while dq:
    x, y = dq.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
            dq.append((nx, ny))
            visited[nx][ny] = True
            board[nx][ny] = board[x][y] + 1

# 출력
for row in board:
    for i in row:
        print(i, end=" ")
    print()


#모든 지점에 대해서 목표지점까지의 거리를 구하여라.
#가로와 세로만 움직인다.
#0은 갈 수 없는 땅
#1은 갈 수 있는 땅
#2는 목표지점

#15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1