from collections import deque

n,m = map(int,input().split())
arr = []
point = [-1,-1]
moves = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    t = list(map(int, input().split()))
    arr.append(t)
    if 2 in t:
        point[0] = i
        point[1] = t.index(2)
        arr[i][t.index(2)]=1


queue = deque()
queue.append((point[0],point[1]))

while queue:
    x,y = queue.popleft()
    for move in moves:
        nx = x+move[0]
        ny = y+move[1]
        ## 리스트 범위
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        ## 못 지나 가는 곳
        if arr[nx][ny]==0:
            continue
        if arr[nx][ny]==1:
            arr[nx][ny] += arr[x][y]
            queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if i==point[0] and j==point[1]:
            print(0,end=' ')
        elif arr[i][j] == 0:
            print(0, end= ' ')
        elif arr[i][j] == 1:
            print(-1, end = ' ')
        else:
            print(arr[i][j]-1,end=' ')
    print()
