import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [0]

for i in range(1, n+1):
    arr.append(i)

def find_parent(val):
    global arr
    if arr[val] == val:
        return val
    p = find_parent(arr[val])
    arr[val] = p
    
    return arr[val]


for _ in range(m):
    op, one, two = map(int, input().split())
    val1 = find_parent(one)
    val2 = find_parent(two)

    if op == 0:
        if val1 < val2:
            arr[val2] = val1
        elif val1 > val2:
            arr[val1] = val2

    else:
        if val1 == val2:
            print("YES")
        else:
            print("NO")