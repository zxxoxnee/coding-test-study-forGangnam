n = int(input())
data = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
min_value = int(1e9)
max_value = -int(1e9)

def solve(i, temp):
    global min_value, max_value
    global plus, minus, multi, div

    if i == n:
        min_value = min(min_value, temp)
        max_value = max(max_value, temp)
        return

    if plus != 0: # plus
        plus -= 1
        solve(i+1, temp+data[i])
        plus += 1
    elif minus != 0: # minus
        minus -= 1
        solve(i+1, temp-data[i])
        minus += 1
    elif multi != 0: #
        multi -= 1
        solve(i+1, temp*data[i])
        multi += 1
    elif div != 0:
        div -= 1
        solve(i+1, int(temp/data[i]))
        div += 1


solve(1, data[0])

print(max_value)
print(min_value)