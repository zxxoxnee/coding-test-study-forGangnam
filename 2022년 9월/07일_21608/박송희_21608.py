import sys
 
input = sys.stdin.readline
n = int(input())
students_list = []
board = [[0 for j in range(n)] for i in range(n)]
dic = {}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
for i in range(n ** 2):
    students_list.append(list(map(int, input().split(" "))))
 
 
def cnt(f_list, i, j):
    count = 0
    f_count = 0
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if board[ny][nx] == 0:
                count += 1
            if f_list:
                if board[ny][nx] in f_list:
                    f_count += 1
    return count, f_count
 
 
for s in students_list:
 
    friend = []
    # board안에 내가 좋아하는 칭구가 있는지 확인해야함
    for i in range(1, 5):
        if s[i] in dic:
            friend.append(s[i])
 
    # 좋아하는 친구가 이미 자리를 잡았을때
    if friend:
        # 모든 자리를 탐색하자
        # 주변에 친한친구 수, 근처 비어있는곳의 갯수, i좌표, j좌표
        max_cnt = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    result, f_cnt = cnt(friend, i, j)
                    if not max_cnt:
                        max_cnt = [f_cnt, result, i, j]
                    if f_cnt > max_cnt[0]:
                        max_cnt = [f_cnt, result, i, j]
                    elif f_cnt == max_cnt[0] and result > max_cnt[1]:
                        max_cnt = [f_cnt, result, i, j]
 
        # 자리를 찾았으면 앉히자
        board[max_cnt[2]][max_cnt[3]] = s[0]
        dic[s[0]] = s[1:]
 
 
    # 친구가 아직 자리를 잡기 전일때
    else:
        # 비어있는 곳의 갯수, i좌표, j좌표
        max_cnt = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    result, f_cnt = cnt(friend, i, j)
                    if not max_cnt:
                        max_cnt = [result, i, j]
                    elif result > max_cnt[0]:
                        max_cnt = [result, i, j]
 
 
        # 자리를 찾았으면 앉히자
        board[max_cnt[1]][max_cnt[2]] = s[0]
        dic[s[0]] = s[1:]
 
# 다 앉힌 후에 점수를 계산하자
# 0:0 / 1:1 / 2:10 / 3:100 / 4:1000
point = 0
for i in range(n):
    for j in range(n):
        f_list = dic[board[i][j]]
        empty_val, f_cnt = cnt(f_list, i, j)
        if f_cnt == 0:
            point += 0
        elif f_cnt == 1:
            point += 1
        elif f_cnt == 2:
            point += 10
        elif f_cnt == 3:
            point += 100
        else:
            point += 1000
 
print(point)