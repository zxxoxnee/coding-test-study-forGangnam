import sys
import math
t = int(sys.stdin.readline())
case = []
for _ in range(t) :
  a = list(map(int, sys.stdin.readline().split()))
  case.append(a)

n = 9999	
array = [True for i in range(n + 1)] 

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1) : 
  if array[i] == True : # 소수
    j = 2
    while i * j <= n :
      array[i * j] = False
      j += 1

for a in case :
  if a[0] == a[1] : 
    print(0)
    continue
  count = 0
  temp = str(a[0])
  for i in range(a[0]+1,a[1]+1) :
    if array[i] == True: 
      c = 0
      for j in range(4) :
        if temp[j] != str(i)[j] : c+=1
        if c > 1 : break
      if c == 1 : 
        temp = str(i)
        print(temp)
        count += 1

  if count == 0 : print('Impossible')
  else : print(count)