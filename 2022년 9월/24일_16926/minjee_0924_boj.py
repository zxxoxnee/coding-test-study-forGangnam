n, m, r = map(int, input().split(' '))
array = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    array.append(data)

# r 회 회전하기
for _ in range(r):
    for i in range(min(n, m)//2):
        x, y = i, i # 맨 처음 좌표 지점
        value = array[x][y] # 맨 처음 좌표가 가진 값
        # 확인방향 맨 좌측 -> 하단 -> 우측 -> 상

        for j in range(i+1, n-i): # left
            x = j
            temp = array[x][y] # 현재 좌표의 값, 바꿀 예정
            array[x][y] = value # 현재 좌표에 이전 값을 넣어준다
            value = temp # 이전 값으로 갱신하기

        for j in range(i+1, m-i): # down
            y = j
            temp = array[x][y]
            array[x][y] = value
            value = temp

        for j in range(i+1, n-i): # right
            x = n - j - 1 # -1 을 해줘야 함 왜냐면 그 이전에 좌표는 예를들어서 n = m = 4 이면 (3,3) 임
            temp = array[x][y] # -1을 해줘야 예전값을 넣을 그 다음 칸을 가리킬 수 있음
            array[x][y] = value
            value = temp

        for j in range(i+1, m-i): # top
            y = n - j - 1
            temp = array[x][y]
            array[x][y] = value
            value = temp

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()
