import sys
from collections import defaultdict

n = int(sys.stdin.readline())
students = defaultdict(list)
for _ in range(n*n) :
  a = list(map(int, sys.stdin.readline().split()))
  students[a[0]] = a[1:]

arr = [[0 * n] for _ in range(n)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

for order in range(n**2):
    student = students[order]
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)