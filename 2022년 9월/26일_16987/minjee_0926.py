# https://www.acmicpc.net/problem/16987
n = int(input())
eggs = [] # 계란 배열
check = [False]*n  # 깨지지 않으면 false, 깨지면 true

for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])

answer = 0
def break_egg(idx): # 계란 부시기
    global answer
    if idx == n:
        count = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                count += 1
        answer = max(count, answer)
        return
    if eggs[idx][0] <= 0: # 지금 손에 있는 계란이 깨진 경우 -> idx+1
        break_egg(idx+1)
        return
    check = True # 계란이 모두 깨져있는지 확인
    for i in range(n):
        if i == idx: # 현재 계란은 pass
            continue
        if eggs[i][0] > 0:
            check = False
            break

    # 계란이 다 깨져있으면 dfs 종료
    if check:
        answer = max(answer, n - 1)
        return

    # 계란 꺠기
    for i in range(n):
        if i == idx:
            continue
        if eggs[i][0] <= 0:
            continue
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        break_egg(idx + 1)
        # back (깨지 않는 경우로 다시 복구)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]

break_egg(0) # index 0 부터 (맨 왼쪽 계란부터 치기 시작)
print(answer)