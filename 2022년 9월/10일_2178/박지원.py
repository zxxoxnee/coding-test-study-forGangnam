'''
특이사항 : 1,1에서 시작!
bfs로 접근해서 풀어보자

1로 계속 타고타고 들어가서,,!
거기서 이제 m까지 도달할 때의 cnt 세자
'''
from collections import deque

#n하고 m입력받기
n,m=map(int,input().split())
#방향그래프
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#배열
p=[]
#n열만큼 반복해서 배열을 만들고, 각각 입력
for _ in range(n):
    p.append(list(input()))

#bfs 함수
def bfs(x,y):
    queue=deque() #우선 큐 초기화
    queue.append((x,y)) #초기 위치 넣어주기

    while queue:
        x,y=queue.popleft()#큐에서 꺼내기

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m: #범위 초과일 경우
                continue
            if p[nx][ny]=='0': #이동할 수 없는 경우
                continue
            if p[nx][ny]=='1': #nx,ny에 처음으로 이동했을 때에,
                p[nx][ny]=int(p[x][y])+1 #p[x][y]는 최소 거리를 저장하고 1을 더할거야.
                queue.append((nx,ny)) #이동된 좌표 넣어주기

    return p[n-1][m-1] #최종 n,m 에 도달한 최소 경로

print(bfs(0,0))
