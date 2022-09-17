N = int(input())

nums = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

print(add,sub,mul,div)
max_num = -1e9
min_num = 1e9


def dfs(i,sum,add,sub,mul,div):
    global max_num, min_num

    if i == N:
        max_num = max(max_num,sum)
        min_num = min(min_num,sum)

    
    if add:
        dfs(i+1,sum+nums[i],add-1,sub,mul,div)
    if sub:
        dfs(i+1,sum-nums[i],add,sub-1,mul,div)
    if mul:
        dfs(i+1,sum*nums[i],add,sub,mul-1,div)
    if div:
        dfs(i+1,int(sum/nums[i]),add,sub,mul,div-1)


dfs(1,nums[0],add,sub,mul,div)

print(max_num)
print(min_num)
