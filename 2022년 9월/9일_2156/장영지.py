
# 다이나믹 프로그래밍??!?
# ㅠㅠ 어렵다

import sys

n = int(sys.stdin.readline())
drink = []
for _ in range(n) :
  a = int(sys.stdin.readline())
  drink.append(a)

dp = [0] * n
dp[0] = drink[0]
dp[1] = drink[0]

# for i in range(3,n) :