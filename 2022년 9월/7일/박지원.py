'''
내 아이디어
1. 비어있는 칸 중 좋아하는 학생이 어디에 있어?(그 칸의 정보)
2. 인접한 칸 중 비어있는 칸
3. 행 번호의 정보, 열 번호의 정보

1->2->3 기준으로 sorted
학생에 대한 정보는 딕셔너리에 담으면 어떨까

'''
#런타임에러
import sys
from collections import defaultdict
input=sys.stdin.readline #이건 메모리용량 줄여보려고 쓸거고
#n 입력받기
n=int(input())
arr = [[0]*n for _ in range(n)]
#좋아하는 학생 딕셔너리
student=defaultdict(list)
#방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]
res=0

#학생 수 입력받기
for _ in range(n*n):
    _input=list(map(int,input().split()))
    student[_input[0]]=_input[1:] #딕셔너리에 저장

    max_x,max_y=0
    max_like,max_empty=-1
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                likecnt=0
                emptycnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] in _input:
                            likecnt+=1 #1번 조건 위해서
                        if arr[nx][ny]==0:
                            emptycnt+=1 #2번 조건 위해서
                if max_like<likecnt or (max_like==likecnt and max_empty<emptycnt): #1번 조건을 만족하거나 2번 조건을 만족하거나
                    max_x=i
                    max_y=j
                    max_like=likecnt
                    max_empty=emptycnt
                    #갱신

        arr[max_x][max_y]=_input[0]#학생 1번쨰의 위치를 우선 이렇게 세팅


#만족도 조사할거야
for i in range(n):
    for j in range(n):
        cnt=0
        like=student[arr[i][j]]#좋아하는 학생
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in like:
                    cnt+=1
        '''
               0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000 
               res+=10**(cnt-1)
              '''
        if cnt!=0:
            res+=10**(cnt-1)

print(res)