n = int(input())
students = [] # 학생에 대한 정보
array = [[0]*n for _ in range(n)]

for _ in range(n*n):
    students.append(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생 자리 배치
for i in range(n*n):

# 학생의 만족도 총 합
result = 0
print(result)