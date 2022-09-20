import sys
from bisect import bisect_left

t = int(sys.stdin.readline())
for _ in range(t) :
  n,m = map(int, sys.stdin.readline().split())
  a = list(map(int, sys.stdin.readline().split()))
  b = list(map(int, sys.stdin.readline().split()))

  a.sort()
  b.sort()
  count = 0

  # for i in a :
  #   for j in b :
  #     if j >= i : break
  #     count += 1
  # print(count)

  for i in a :
    count += bisect_left(b,i)
  print(count)
