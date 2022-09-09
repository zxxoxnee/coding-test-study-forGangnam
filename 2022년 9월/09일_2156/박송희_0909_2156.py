import sys
sys.stdin = open("20220909_2156_포도주.txt", "r")

n = int(input())
w = []

for _ in range(n) :
    num = int(input())
    w.append(num)

dp = [0] * n

dp[0] = w[0]                  #초기값세팅

if n > 1 :
    dp[1] = w[0] + w[1]

if n > 2 :
    dp[2] = max(w[2] + w[1], w[2] + w[0], dp[1])

for i in range(3, n) :
    dp[i] = max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i])

print(dp[n-1])

#포도주 잔이 일렬
#포도주 잔을 선택
#그 잔에 들어있는 포도주는 모두 마심
#마신 후에는 원래 위치에 다시 놓아야 한다.


#연속으로 놓여 있는 3잔을 모두 마실 수는 없다.