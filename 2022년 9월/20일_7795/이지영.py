### 이건 메모리 초과 발생
# from itertools import product
# T = int(input())
# result = []
# for _ in range(T):
#     answer = 0
#     n,m = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     combinations = list(product(a,b))
#     for c in combinations:
#         if c[0]>c[1]:
#             answer+=1
#     result.append(answer)

# for r in result:
#     print(r)

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    start = 0
    count = 0
    for j in range(n):
        while True:
            if start == m or a[j]<=b[start]:
                count+=start
                break
            else:
                start+=1
    print(count)