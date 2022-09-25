import sys

t = int(sys.stdin.readline())
for i in range(t) :
  n = int(sys.stdin.readline())
  if n == 0 : 
    print("Case #"+str(i+1)+": INSOMNIA")
    continue
  count = 0
  l = 0
  visit = [0] * 10
  while l < 10 :
    count += 1
    temp = n * count 
    while temp != 0 :
      if visit[temp % 10] == 0 :
        visit[temp % 10] = 1
        l += 1
      temp //= 10

  print("Case #"+str(i+1)+": "+str(n*count))