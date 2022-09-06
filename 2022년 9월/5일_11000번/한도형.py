import heapq
n = int(input())
timelist = [list(map(int, input().split())) for _ in range(n)]
timelist.sort()

timequeue = []
heapq.heappush(timequeue, timelist[0][1])
# print(timequeue.get())
for i in range(1,n):
    # 시작시간이 더 이르면 겹침
    if timelist[i][0] < timequeue[0]:
        heapq.heappush(timequeue, timelist[i][1])
    else:
        heapq.heappop(timequeue)
        heapq.heappush(timequeue, timelist[i][1])
print(len(timequeue))