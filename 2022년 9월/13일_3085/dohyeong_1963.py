n = int(input())
graph = [list(input()) for _ in range(n)]
ans = 0

def check():
    global ans
    for i in range(n):
        cnt = 1
        for j in range(0,n-1):
            if graph[i][j] == graph[i][j+1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
        cnt = 1
        for j in range(0,n-1):
            if graph[j][i] == graph[j+1][i]
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

