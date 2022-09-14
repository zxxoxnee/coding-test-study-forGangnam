from collections import deque
# bfs 로 풀이

n, m = map(int, input().split())
array = []
sx, sy = 0, 0
for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    for j in range(m):
        if data[j] == 2:
            sx = i
            sy = j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)] # 방문 여부를 기억해 두어야 나중에 통과할 수 있지만 방문하지 못한 부분을 -1로 바꿀 수 있

def bfs(a, b):
    queue = deque()
    queue.append((a, b)) # 시작 지점
    array[a][b] = 0 # 0으로 바꾸기 -> 0으로 바꿔야 나중에 거리 메모이제이션하는것이 편하다
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 세로 가로 이동 가능 = 상하좌우 이동 가능
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] != 0 and visited[nx][ny] == False:
                    array[nx][ny] = array[x][y] + 1 # 새롭게 방문하는 자점의 거리 : 이전거리 + 1
                    visited[nx][ny] = True # 방문 여부 확인
                    queue.append((nx, ny))


bfs(sx, sy)
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and array[i][j] == 1:
            print(-1, end=' ')
        else:
            print(array[i][j], end=' ')
    print()



