import sys

n,k = map(int,sys.stdin.readline().split())
coin = []
for _ in range(n) :
  a = int(sys.stdin.readline())
  if a <= k :
    coin.append(a)

dp = [0 for n in range(k+1)] # 가치의 합이 n이 되는 경우의 수
# dp[0] = 1

for c in coin :
  dp[c] += 1
  for j in range(c,k+1) :
    if j-c >= 0 :
      dp[j] += dp[j-c]

print(dp[k])
