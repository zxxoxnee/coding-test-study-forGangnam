from collections import deque
import queue

N,M = map(int,input().split(' '))
maze = []
move = [(-1,0),(1,0),(0,-1),(0,1)]

##최단거리는 bfs
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maze[nx][ny]==0:
                continue
            if maze[nx][ny] ==1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx,ny))
    
    print(maze[N-1][M-1])






for _ in range(N): 
    maze.append(list(map(int,input())))

bfs(0,0)





