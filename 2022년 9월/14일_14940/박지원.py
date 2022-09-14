'''
우선, 이 문제의 가장 큰 아이디어는 bfs!
하나의 시작점 ~ 모든 지점까지 거리 구할거니까!
자료구조는 deque 활용 !
'''
from collections import deque

#n,m 입력
n,m= map(int,input().split())

box=[0 for _ in range(n)]
#목표지점
gr,gc=0,0
for i in range(n):
    box[i]=list(map(int,input().split()))
    for j in range(len(box[i])):
        if box[i][j]==2:
            gr,gc=i,j

#답 출력할 리스트
ans=[[-1 for _ in range(m)] for _ in range(n)] #방문할 수 없는 곳은 -1로 나와야하니까

#원래 갈 수 없는 위치는 0
for i in range(n):
    for j in range(m):
        if box[i][j]==0:
            ans[i][j]=0

#방문 리스트
visited=[[False for _ in range(m)]for _ in range(n)]

#bfs 활용하자
q=deque([[gr,gc,0]])
ans[gr][gc]=0
dx=[-1,1,0,0]
dy=[0,0,1,-1]

while q:
    t=q.popleft()
    cr,cc,cnt=t[0],t[1],t[2]
    if visited[cr][cc]:
        continue
    visited[cr][cc]=True
    for d in range(4):
        nx=cr+dx[d]
        ny=cc+dy[d]
        if 0<=nx < n and 0<=ny<m and not visited[nx][ny]:
            if box[nx][ny]==1:
                ans[nx][ny]=cnt+1
                q.append([nx,ny,cnt+1])

#출력
for i in range(n):
    print(*ans[i])


'''
#이 코드로는 출력 초과 뜸

box=[] #입력값을 저장
queue=deque([])
visited=[[False]*m for _ in range(n)] #탐색 여부 저장할 리스트
result=[[-1]*m for _ in range(n)] #최종 결과값을 저장할 리스트

for i in range(n):
    row=list(map(int,input().split()))
    for j in range(m):
        # 목표 지점 찾기
        if row[j]==2:
            queue.append((i,j))
            visited[i][j]=True
            result[i][j]=0

        #벽 기록
        if row[j]==0:
            result[i][j]=0
    box.append(row)

# BFS 탐색
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우
while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and box[nx][ny] == 1:
            queue.append((nx, ny))
            visited[nx][ny] = True
            result[nx][ny] = result[x][y] + 1

    #출력
    for row in result:
        for i in row:
            print(i,end=" ")
        print()
'''
