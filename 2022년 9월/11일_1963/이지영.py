import math
from collections import deque


def bfs(s,e):
    queue = deque()
    queue.append(s)

    visited = [0 for _ in range(10000)] 
    visited[s] = 1
    while queue:
        n = queue.popleft()
        for i in range(4):
            for j in range(10):
                x = list(str(n))
                x[i] = str(j)
                t = int("".join(x))
                if visited[t] == 0 and primeNumber[t] and t>1000:
                    visited[t] = visited[n]+1
                    queue.append(t)
    return visited[e]

testCase = int(input())

primeNumber = [1 for _ in range(10000)]

result = []

for i in range(2,int(math.sqrt(10000))):
    for j in range(i*2,10000,i):
        primeNumber[j]=0 
    
for _ in range(testCase):
    N,M = map(int,input().split())
    
    result.append(bfs(N,M))

for r in result:
    print(r-1)
