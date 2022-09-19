import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
nums = []
for _ in range(n) :
  a = int(sys.stdin.readline())
  nums.append(a)

stack = []
def cal(a,b,c) :
  if c == '+' :
    return a + b
  elif c == '-' :
    return a - b
  elif c == '*' :
    return a * b
  else :
    return a/b


for i in s :
  if i.isalpha() :
    stack.append(nums[ord(i)-65])
  else :
    a = stack.pop()
    b = stack.pop()
    stack.append(cal(b,a,i))

print(format(stack.pop(),".2f"))