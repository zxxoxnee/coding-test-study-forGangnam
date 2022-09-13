# 3085

n = int(input())
array = []
for _ in range(n):
    array.append(list(input()))

result = 0 #

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def count():
    result = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            # 가로 확인
            if array[i][j] == array[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            result = max(cnt, result)

        cnt = 1
        for j in range(1,n):
            if array[j-1][i] == array[j][i]:
                cnt += 1
            else:
                cnt = 1
            result = max(cnt, result)
    return result

answer = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            if array[i][j] != array[i][j+1]:
                array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
                answer = max(count(), answer)
                array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
        if i+1 < n:
            if array[i][j] != array[i+1][j]:
                array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
                answer = max(count(), answer)
                array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]

print(answer)