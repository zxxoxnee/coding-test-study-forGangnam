import sys
import heapq

n = int(sys.stdin.readline())
clss = []
for _ in range(n) :
  s,t = map(int,sys.stdin.readline().split())
  clss.append([s,t])

clss.sort()
hq = []
for i in clss :
  if hq and hq[0] <= i[0]:
    heapq.heappop(hq) 
  heapq.heappush(hq, i[1])
# print(hq)
print(len(hq))