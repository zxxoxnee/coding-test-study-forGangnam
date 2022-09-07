N = int(input())

classRoom = [[0 for _ in range(N)] for _ in range(N)]
students = {}
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
score = [0, 1, 10, 100, 1000]
result = 0

for _ in range(N*N):
    s = list(map(int, input().split(' ')))
    students[s[0]] = s[1:5]

for s, likes in students.items():
    candidates = []
    for i in range(N):
        for j in range(N):
            if classRoom[i][j] == 0:
                empty = 0
                like = 0
                for m in moves:
                    r = i+m[0]
                    c = j+m[1]
                    if r < N and c < N and r > -1 and c > -1:
                        if classRoom[r][c] == 0:
                            empty += 1
                        elif classRoom[r][c] in likes:
                            like += 1
                        candidates.append([like, empty, i, j])
    candidates.sort(key=lambda x: (x[0], x[1], -x[2], -x[3])) ##이차원 리스트 정렬은 이렇게 key:lamda x:(요소 조건) ,,, 만약 reverse 원하면 - 달기

    classRoom[candidates[-1][2]][candidates[-1][3]] = s


for i in range(N):
    for j in range(N):
        like = 0
        for m in moves:
            r = i+m[0]
            c = j+m[1]
            if r < N and c < N and r > -1 and c > -1:
                if classRoom[r][c] in students[classRoom[i][j]]:
                    like += 1
        result += score[like]

print(result)
