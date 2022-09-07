n = int(input())
students = [] # 학생에 대한 정보
array = [[0]*n for _ in range(n)]

for _ in range(n*n):
    students.append(map(int, input().split()))

