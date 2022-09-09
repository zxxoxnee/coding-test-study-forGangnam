'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
 
첫째 줄에 N이 주어진다. 둘째 줄부터 N^2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.

학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 
입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N^2보다 작거나 같은 자연수이다. 
어떤 학생이 자기 자신을 좋아하는 경우는 없다.

이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다.
학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 
그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.

출력
첫째 줄에 학생의 만족도의 총 합을 출력한다.
제한
3 ≤ N ≤ 20

예제 입력 1  복사
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
예제 출력 1  복사
54

'''
import heapq

n = int(input())

pos_students = [[] for _ in range(n*n+1)]
pan = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def select_pos(s, l, i, k ,e, pan):
    pan_for_select = []
    # 비어있는 
    for x in range(n):
        for y in range(n):
            if pan[x][y] != 0:
                continue
            else:
                cnt_student = 0
                cnt_empty = 0

                for z in range(4):
                    if 0 <= x + dx[z] < n and 0 <= y + dy[z] < n:
                        if pan[x + dx[z]][y + dy[z]] == l or pan[x + dx[z]][y + dy[z]] == i or pan[x + dx[z]][y + dy[z]] == k or pan[x + dx[z]][y + dy[z]] == e:
                            cnt_student += 1
                        
                        elif pan[x + dx[z]][y + dy[z]] == 0:
                            cnt_empty += 1

                heapq.heappush(pan_for_select, (-cnt_student, -cnt_empty, x, y))
    
    tmp_1, tmp_2, x, y = heapq.heappop(pan_for_select)
    pan[x][y] = s

                

for c in range(n*n):
    s, l, i, k, e = map(int, input().split())
    pos_students[s].extend([l, i, k, e])
    
    select_pos(s, l, i, k, e, pan)

for x in range(n):
    for y in range(n):
        cnt = 0
        val = pan[x][y]
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                if pan[x + dx[i]][y + dy[i]] in pos_students[val]:
                    cnt += 1

        if cnt == 0:
            ans += 0
        elif cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)


 