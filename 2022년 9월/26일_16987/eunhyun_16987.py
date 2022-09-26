n = int(input())
ans = -1
arr = [list(map(int, input().split())) for _ in range(n)]

def solve(pos, arr, cnt):
    global ans

    if pos == n:
        ans = max(ans, cnt)
        return

    if arr[pos][0] <= 0:
        solve(pos+1, arr, cnt)
        return

    else:
        if cnt == n-1:
            ans = max(ans, cnt)
            return
        for i in range(n):
            if i == pos or arr[i][0] <= 0:
                continue
            tmp_arr = arr[:]
            tmp_arr[pos][0] -= arr[i][1]
            tmp_arr[i][0] -= arr[pos][1]

            if tmp_arr[pos][0] <= 0:
                cnt += 1
            if tmp_arr[i][0] <= 0:
                cnt += 1

            solve(pos+1, tmp_arr, cnt)


solve(0, arr, 0)
print(ans)