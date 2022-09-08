'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1  복사
4 6
101111
101010
101011
111011
예제 출력 1  복사
15

'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

pan = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
q.append((0,0))
visited[0][0] = pan[0][0]

while q:
    x, y = q.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < m and pan[new_x][new_y] != 0:
            if visited[new_x][new_y] == 0:
                visited[new_x][new_y] = visited[x][y] + pan[new_x][new_y]
                q.append((new_x, new_y))
            
            else:
                if visited[new_x][new_y] > visited[x][y] + pan[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + pan[new_x][new_y]
                    q.append((new_x, new_y))
                
print(visited[n-1][m-1])