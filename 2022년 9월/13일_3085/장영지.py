## 모든 경우의 수 확인하기??

import sys

n = int(sys.stdin.readline())
candy = []
for _ in range(n) :
  a = list(sys.stdin.readline().strip())
  candy.append(a)
# print(candy)

def check(arr) : # 가장 긴 연속된 부분 찾기
  result = 1
  for i in range(n) :
    cnt = 1
    for j in range(1,n) :
      if arr[i][j] == arr[i][j-1] :
        cnt += 1
      else : 
        cnt = 1
      result = max(result,cnt)

    cnt = 1
    for j in range(1,n) :
      if arr[j][i] == arr[j-1][i] :
        cnt += 1
      else : 
        cnt = 1
      result = max(result,cnt)
  return result


result = 0
for i in range(n) :
  for j in range(n) :
    # 한쪽 방향으로만 바꾸면 중복없이 확인 가능
    if j + 1 < n and candy[i][j] != candy[i][j+1]:
      candy[i][j], candy[i][j+1] = candy[i][j+1],candy[i][j]
      result = max(result, check(candy))
      candy[i][j], candy[i][j+1] = candy[i][j+1],candy[i][j]
    
    if i + 1 < n and candy[i][j] != candy[i+1][j] :
      candy[i][j], candy[i+1][j] = candy[i+1][j],candy[i][j]
      result = max(result, check(candy))
      candy[i][j], candy[i+1][j] = candy[i+1][j],candy[i][j]
    
print(result)