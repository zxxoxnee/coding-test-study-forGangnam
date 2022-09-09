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
time=[]

#강의시간 리스트로 입력받기
for _ in range(n):
    s, t = map(int, input().split())
    time.append((s, t))

#리스트 정렬
time.sort()
sr=[] #강의실(우선순위큐)
heapq.heappush(sr,time[0][1]) #우선순위큐에 우선 첫 시작시간에 문 여는 강의실 문 열기

for i in range(1,n):
    if time[i][0] >= sr[0]:
        heapq.heappop(sr)#새로운 회의로 시간 변경해야할거니까(즉, 갯수는 똑같게)
        heapq.heappush(sr,time[i][1])#새 시간 push
    else:
        heapq.heappush(sr,time[i][1])

print(len(sr))
