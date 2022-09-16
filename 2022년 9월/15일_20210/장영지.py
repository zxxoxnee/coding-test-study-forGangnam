# 정렬문제,,,,,
# 문자를 쪼개서 확인 ? 인덱스로??

import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n) :
  s = sys.stdin.readline().strip()
  arr.append(s)

arr.sort()

for i in arr :
  print(i)