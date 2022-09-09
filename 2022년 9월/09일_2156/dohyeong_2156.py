'''
가능한 경우
1 <= n <= 10000
1. i-2까지  최대값에 i 와인
2. i-3까지 최대값에 i-1, i와인
3. i-1까지 최대값에 i와인 안먹음
'''

n = int(input())
data = [0] * 10000
d = [0] * 10000
for i in range(n):
    data[i] = int(input())

d[0] = data[0]
d[1] = data[1] + data[0]
d[2] = max(d[1], d[2] + d[0], d[2] + d[1])

for i in range(3,n):
    d[i] = max(d[i-1], d[2] + d[0], d[2] + d[1])

print(max(d))