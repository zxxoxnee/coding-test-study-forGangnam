# 7795
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    # a가 b보다 큰 쌍의 개수
    array_a.sort(reverse=True)
    array_b.sort()
    count = 0
    for i in range(n):
        if i > 0 and array_a[i] == array_a[i-1]:
            continue
        for j in range(m):
            if j > 0 and array_b[j] == array_b[j-1]:
                continue
            if array_a[i] > array_b[j]:
                count += 1
    print(count)
