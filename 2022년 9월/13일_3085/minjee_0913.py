# 3085

n = int(input())
array = []
for _ in range(n):
    array.append(list(input()))

result = 0 #

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def count(n):
    result = 1
    for i in range(1, n):
        cnt = 1
        for j in range(1,n):
            # 가로 확인
            if array[i][j] == array[i][j-1]:
                cnt += 1
            else:
                result = max(cnt, result)
        cnt = 1
        for j in range(1,n):
            if array[j-1][i] == array[j][i]:
                cnt += 1
            else:
                result = max(cnt, result)
    return result

answer = 1
for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if array[x][y] != array[nx][ny]: # 인접한 두 사탕이 다른 경우
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y] # 교환한다
                    answer = max(count(n), answer)
                    # 다시 원래 위치
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]

# 가로 세로 확인하기


print(answer)