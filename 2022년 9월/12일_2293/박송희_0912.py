import sys
sys.stdin = open("20220911_2293_동전1.txt", "r")

n, k = map(int, input().split())
numList = []

for i in range(n) :
    num = int(input())
    numList.append(num)

dp = [0] * (k + 1)
dp[0] = 1

for i in numList :
    for j in range(i, k+1) :
        if j - i >= 0 :
            dp[j] += dp[j-i]

print(dp)
print(dp[k])

