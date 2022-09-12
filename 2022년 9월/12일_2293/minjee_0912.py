n, k = map(int, input().split())
coins = []
dp = [0] * (k+1)
dp[0] = 1 # 예외처리를 위한 dp값 초기화 ex) dp[1] = dp[1] + dp[0]

# 경우의 수 구하기
for _ in range(n):
    coins.append(int(input()))

for coin in coins: # 1, 2, 5 값 돌아가면서 확인하기
    for i in range(1 , k+1): # 합이 k가 되는것을 찾아야 함
        if coin <= i: # i 는 부분합
            dp[i] += dp[i - coin] # dp 에 결과값을 쌓아야 함 (1), (1, 2), (1, 2, 5)

print(dp[k])
