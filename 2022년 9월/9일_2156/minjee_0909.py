# [Boj] 2156 포도주 시식
n = int(input())
data = [0] # 포도주
for i in range(n):
    data.append(int(input()))
dp = [0]*(n+1)
dp[1] = data[1]
if n > 1: # 포도주 잔이 2개 이상인 경우
    dp[2] = dp[1] + data[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+data[i], dp[i-3]+ data[i] + data[i-1]) # 근데 4번째부터 조심해야하는데...
print(dp[n]) # 최대값