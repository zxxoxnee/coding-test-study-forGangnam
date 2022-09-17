n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
res = [[0] * m for _ in range(n)]
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# dfs 활용해서 조합, 바이러스 퍼뜨리기 둘다 해결

# 바이러스 시작점에서 퍼지는 메서드
def spread(x,y):
    for i in range(4):
        nx, ny = x + dx(i), y + dy(i)
        if 0<=nx<n and 0<=ny<m:
            if res[nx][ny] == 0:
                res[nx][ny] = 2
                spread(nx,ny)

def dfs(cnt):
    global ans
    # 종료 조건 울타리 3개
    if cnt ==3:
        for i in range(n):
            for j in range(m):
                res[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if res[i][j] == 2:
                    spread(i,j)

        num = 0
        for i in range(n):
            for j in range(m):
                if res[i][j] == 0:
                    num += 1
        ans = max(ans, num)
        return
    # 울타리 설치 dfs로 구현
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)

