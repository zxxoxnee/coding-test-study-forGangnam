import sys

n,k = map(int,sys.stdin.readline().split())
coin = []
for _ in range(n) :
  a = int(sys.stdin.readline())
  coin.append(a)

dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin :
  for j in range(c,k+1) :
    if j-c >= 0 :
      dp[j] += dp[j-c]

print(dp[k])
