# T = int(input())
# res = 0
# for _ in range(T):
#     N,M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     cnt = 0
#     A.sort()
#     B.sort()
#     for i in A:
#         while True:
#             if cnt == M or i <= B[cnt]:
#                 break
#             else:
#                 cnt += 1
#     res += cnt
#     print(res)

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    # 각 i에 대한 카운트
    count = 0
    # 전체 합
    res = 0

    for i in range(N):
        while True:
            if count == M or A[i] <= B[count]:
                res += count
                break
            else:
                count += 1

    print(res)