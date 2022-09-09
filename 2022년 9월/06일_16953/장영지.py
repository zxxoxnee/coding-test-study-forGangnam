import sys

a,b = map(int,sys.stdin.readline().split())
count = 0
while b > a :
  while str(b)[-1] == '1' :
    b = str(b)
    b = int(b[:len(b)-1])
    count += 1
    if b <= a : break
  if b <= a : break
  if b % 2 != 0 : 
    print(-1)
    exit(0)
  b = b//2
  count += 1

# print(a,b)
if a == b : print(count+1)
else : print(-1)

### 반례 찾는 중ㅜㅜㅜ