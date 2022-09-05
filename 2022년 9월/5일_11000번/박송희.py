import sys
#sys.stdin = open("20220906_타임어택_백준_11000_강의실배정.txt", "r")
import heapq

n = int(input())
time = []

for _ in range(n) :
    start, end = map(int, input().split())
    time.append([start, end])

#끝나는 시간으로 오름차순 정렬
time.sort()

heap = []

for i in range(n) :
    if len(heap) != 0 and heap[0] <= time[i][0] :
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))