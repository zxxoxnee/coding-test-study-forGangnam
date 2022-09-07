n = int(input())
graph = [[0] * n for _ in range(n)]

students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for student in students:
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] in student:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                temp.append([i,j,like, blank])
    temp.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
    graph[temp[0][0]][temp[0][1]] = student[0]

answer = 0
students.sort()
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] in students[graph[i][j]-1]:
                    cnt += 1
        if cnt > 0:
            answer += 10 ** (cnt-1)
print(answer)