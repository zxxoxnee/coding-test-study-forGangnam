# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0

    def attack(a, b, c, d, degree):
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                board[i][j] -= degree

    def save(a, b, c, d, degree):
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                board[i][j] += degree

    n = len(board)
    m = len(board[0])

    for data in skill:
        if data[0] == 1:
            attack(data[1], data[2], data[3], data[4], data[5])
        else:
            save(data[1], data[2], data[3], data[4], data[5])
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 1:
                answer += 1
    return answer

# 효율성을 어떻게 개선하지 ????