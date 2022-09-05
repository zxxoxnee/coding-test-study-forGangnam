import heapq

n = int(input())

time = []

for _ in range(n):
    s, t = map(int, input().split())
    time.append((s, t))

queue = []
time.sort()
heapq.heappush(queue, time[0][1]) # 강의 끝나는 시간, 강의실 수
for i in range(1, n):
    if time[i][0] >= queue[0]:
        heapq.heappop(queue) # 큐에서 똑같은 강의실을 뺐다가 다시 넣기
        heapq.heappush(queue, time[i][1])
    else:
        heapq.heappush(queue, time[i][1])

print(len(queue))



