n,k = map(int,input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

## 점화식 세우기 어렵다..

dp = [0 for _ in range(k+1)]
dp[0]=1

for i in range(n):
    for j in range(coins[i],k+1):
        dp[j] += dp[j-coins[i]]


print(dp[j])
