n = int(input())

data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_ = 1e9
max_ = -1e9

def dfs(cnt, value):
    global min_, max_, add, sub, mul, div

    if cnt == n:
        min_ = min(min_, value)
        max_ = max(max_, value)

    else:
        if add > 0:
            add -= 1
            dfs(cnt+1, value + data[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt+1, value - data[cnt])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(cnt+1, value * data[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt+1, int(value / data[cnt]))
            div += 1
dfs(1, data[0])

print(max_)
print(min_)
