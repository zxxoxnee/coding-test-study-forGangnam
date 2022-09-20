# 7795
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    # a가 b보다 큰 쌍의 개수
    array_a.sort()
    array_b.sort()
    count = 0
    j = 0
    for i in range(n):
        while True:
            if j == m or array_a[i] <= array_b[j]:
                count += j
                break
            else:
                j += 1
    print(count)
