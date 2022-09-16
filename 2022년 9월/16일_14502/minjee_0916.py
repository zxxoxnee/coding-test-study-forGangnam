# 14502 연구소
import copy

n, m = map(int, input().split())
array = []
temp = [[0] *m for _ in range(n)] # 바이러스 퍼지는거 확인하기 위해서

for i in range(n):
    array.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바이러스 퍼뜨리는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 # new virus
                virus(nx, ny)

answer = 0

def check():
    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1
    return result

# 벽 3개
def block(count):
    global answer
    if count == 3: # 벽 세개인 경우 검증하기
        for i in range(n):
            for j in range(m):
                temp[i][j] = array[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        answer = max(answer, check()) # 최대값으로 갱신하기
        return

    # 벽 개수가 아직 3개 미만인 경우 -> 벽을 추가한다 , 백트래킹
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                count += 1
                block(count)
                array[i][j] = 0 # 다시 back
                count -= 1

block(0)
print(answer)