import sys

s = sys.stdin.readline().strip()
result = ''
temp = ''
flag = False
for i in s :
  if i == '<' : 
    flag = True
    result += temp[::-1]
    result += i
    temp = ''
  elif i == '>' : 
    flag = False
    result += i

  elif not flag :
    if i == ' ' and temp :
      result += temp[::-1]
      temp = ''
      result += i
    else :
      temp += i
  elif flag : 
    result += i
  
if temp : result += temp[::-1]
print(result)