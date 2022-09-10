# https://www.acmicpc.net/problem/1963

def solve(a, b):
    array = [True] * (b+1)
    result = 0
    for i in range(a, b+1):
        if array[i]:
            j = 2
            while i*j < b:
                array[i*j] = False
                j += 1
    num = a
    # array들 중에서 숫자가 하나만 다른것 찾기
    # 걸러낸 a~b 사이 소수들 중에서 최단거리 찾기

    if num == b:
        return result
    else:
        return -1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = solve(a, b)
    if result >= 0:
        print(result)
    else:
        print('Impossible')

