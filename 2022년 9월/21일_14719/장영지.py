import sys

h,w = map(int,sys.stdin.readline().split())
block = list(map(int,sys.stdin.readline().split()))

result = 0

for i in range(1, w - 1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    compare = min(left_max, right_max)

    if block[i] < compare:
        result += compare - block[i]

print(result) 
  
  
  
  