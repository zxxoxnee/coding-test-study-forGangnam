import sys
from collections import deque

# set prime table
prime = [1] * 10001
for i in range(2, 5000):
    t = 2
    while i*t < 10000:
        prime[i*t] = 0
        t += 1

def bfs():
    queue = deque([(first, 0)])
    while queue:
        now, step = queue.popleft()
        if now == last:
            return step
        
        NOW = str(now)
        step += 1
        for i in range(4):
            for j in map(str, range(10)):
                if i == 0 and j == '0':
                    continue
                num = int(NOW[:i] + j + NOW[i+1:])
                if prime[num] and not visited[num]:
                    visited[num] = 1
                    queue.append((num, step))

for _ in range(int(sys.stdin.readline())):
    first, last = map(int, sys.stdin.readline().split())
    visited = [0] * 10001
    print(bfs())