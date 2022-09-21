import sys

input = sys.stdin.readline
h, w = map(int, input().split())
block = list(map(int, input().rstrip().split(' ')))
max_height, max_index, block_sum = 0, 0, 0
for i in range(w):
    block_sum += block[i]
    if max_height < block[i]:
        max_height =block[i]
        max_index = i

total = 0
tmp = 0
# 왼쪽에서 가장 높은 블록까지
for i in range(max_index + 1):
    if tmp <block[i]:
        tmp =block[i]
    total += tmp
tmp = 0
# 오른쪽에서 가장 높은 불록까지(높은 블록은 범위에서 제외)
for i in range(w-1, max_index, -1):
    if tmp < block[i]:
        tmp =block[i]
    total += tmp

print(total-block_sum)