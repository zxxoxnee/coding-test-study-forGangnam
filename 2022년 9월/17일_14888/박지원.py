import sys
input = sys.stdin.readline

n=int(input())
a_box=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

maxans, minans = -sys.maxsize -1, sys.maxsize

def backtracking(a,i,add,sub,mul,div):
    global maxans, minans
    #종료 조건
    if i==n:
        maxans=max(maxans,a)
        minans=min(minans,a)
        return

    if add>0:
        backtracking(a+a_box[i],i+1,add-1,sub,mul,div)
    if sub>0:
        backtracking(a-a_box[i],i+1,add, sub-1, mul, div)
    if mul>0:
        backtracking(a*a_box[i],i+1,add, sub, mul-1, div)
    if div>0:
        backtracking(int(a/a_box[i]),i+1,add, sub, mul, div-1)



backtracking(a_box[0],1,add,sub,mul,div)
print(maxans)
print(minans)
