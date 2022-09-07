n = int(input())
students = [] # 학생에 대한 정보
array = [[0]*n for _ in range(n)]

for _ in range(n*n):
    students.append(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0 # 만족도
# 학생 자리 배치
for student in students:
    temp = []
    for x in range(n):
        for y in range(n):
            empty = 0
            like = 0  # 좋아하는 학생
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n*n and 0 <= ny < n*n:
                    if array[nx][ny] == 0:
                        empty += 1
                    elif array[nx][ny] in student[1:]:
                        like += 1
            temp.append((empty, like, x, y))

    temp.sort()
    nx, ny = temp[0][2], temp[0][3]
    array[nx][ny] = student[0] # 현재 배치하는 학생
    result += temp[0][1]

print(result)

