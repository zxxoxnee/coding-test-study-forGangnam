n = int(input())

array = [[0]*n for _ in range(n)]
student_dict = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0 # 만족도
for i in range(n*n):
    data = list(map(int, input().split()))
    student_dict[data[0]] = data[1:]
    max_x, max_y = 0, 0
    max_like = -1
    max_empty = -1

    for x in range(n):
        for y in range(n):
            if array[x][y] == 0: # 빈자리인지 우선 체크
                like = 0
                empty = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if array[nx][ny] == 0: # 빈자리
                            empty += 1
                        if array[nx][ny] in student_dict[data[0]]: # 좋아하는 학생
                            like += 1
                if max_like < like or (max_empty < empty and max_like == like):
                    max_x, max_y = x, y
                    max_like = like
                    max_empty = empty
    array[max_x][max_y] = data[0]

for i in range(n):
    for j in range(n):
        like = 0
        like_student = student_dict[array[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] in like_student:
                    like += 1
        if like > 0:
            result += 10**(like-1)

print(result)

