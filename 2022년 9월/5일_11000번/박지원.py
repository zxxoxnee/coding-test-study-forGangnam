'''
우선순위 큐를 사용해보는 건 어떨까?

**현재 회의실의 종료시간과 다음 열릴 회의의 시작 시간을 비교
1. 회의 종료 시간보다 회의 시작 시간이 빠르면 회의실 하나 추가
2. 만약 회의 종료 시간보다 시작시간이 느리면 이어서 가능

[시작, 끝] <-- 리스트에 추가
시작 기준 정렬(빠른 순)

'''

import heapq
#n입력받기
n=int(input())
#우선순위 큐
queue=[]
#시작시간 종료시간 입력받기
for i in range(n):
    start,end=map(int,input().split())
    queue.append([start,end]) #쌍으로 리스트에 넣어주기

sr=[] #강의실
heapq.heappush(sr,queue[0][1]) #우선순위큐에 우선 첫 시작시간에 문 여는 강의실 문 열기

for i in range(1,n):
    if queue[i][0]<sr[0]:#회의 종료 시간보다 다음 회의 시간이 빠르다면
        heapq.heappush(sr,queue[i][1]) #새로운 강의실 개설
    else:#회의 종료 시간보다 다음 회의 시간이 늦다면, (즉 연장으로 강의실 가능)
        heapq.heappop(sr)#새로운 회의로 시간 변경해야할거니까(즉, 갯수는 똑같게)
        heapq.heappush(sr,queue[i][1])#새 시간 push


print(len(sr))
