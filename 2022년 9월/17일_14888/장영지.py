from itertools import permutations
import sys

t = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
o = list(map(int,sys.stdin.readline().split()))

a =['a']*o[0]
b =['b']*o[1]
c =['c']*o[2]
d =['d']*o[3]

o_list = a+b+c+d
o_list = list(permutations(o_list,t-1))
o_list = list(set(o_list))

result = []

def cal(x,y,o) :
    if o == 'a' :
        return x+y
    elif o == 'b' :
        return x-y
    elif o == 'c' :
        return x*y
    else : 
        if x < 0 :
            return (abs(x)//y)*-1
        else :
            return x//y
        
for i in o_list :
    r = x[0]
    for j in range(1,t) :
        r = cal(r,x[j],i[j-1])
        if j == t-1 :
            result.append(r)

print(max(result))
print(min(result))