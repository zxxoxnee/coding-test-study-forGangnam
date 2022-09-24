''''
예제 입력 1  복사
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

예제 출력 1  복사
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
'''
from collections import deque
n, m, r = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def val_rotate(pan, visited, x, y, d, s, cn, cm):

    q = deque()
    q.append((x,y,d))

    while q:
        x, y, d = q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        
        if s > nx or nx >= cn or s > ny or ny >= cm:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        if visited[nx][ny] != -1:
            break

        visited[nx][ny] = pan[x][y]
        q.append((nx, ny, d))


for _ in range(r):
    visited = [[-1] * m for _ in range(n)]
    p = 0
    for x in range(n // 2):
        for y in range(m // 2):
            if x != y:
                continue
            val_rotate(pan, visited, x, y, 0, 0 + p, n - p, m - p)
            p += 1

    pan = [visited[i][:] for i in range(n)]
                  
for i in range(n):
    print(*visited[i])