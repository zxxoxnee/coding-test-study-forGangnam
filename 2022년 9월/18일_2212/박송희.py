import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
array = list(map(int, input().split()))

array.sort()
dist = []
for i in range(n-1):
    dist.append(array[i+1] - array[i])
dist.sort(reverse=True)
    
print(sum(dist[k-1:]))