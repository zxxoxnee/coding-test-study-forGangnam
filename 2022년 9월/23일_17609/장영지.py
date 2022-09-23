import sys

t = int(sys.stdin.readline())

for _ in range(t) :
  s = sys.stdin.readline().strip()
  if s ==  s[::-1] :
    print(0)
  else :
    for i in range(len(s)) :
      # if s.count(i) == 1 :
      #   # s[]
