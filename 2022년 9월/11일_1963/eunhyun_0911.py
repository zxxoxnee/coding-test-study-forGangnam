'''
소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 
어느 날 창영이는 친한 친구와 대화를 나누었는데:

“이제 슬슬 비번 바꿀 때도 됐잖아”
“응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
“그럼 8179로 해”
“흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 
예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 여러 단계를 거쳐야 만들 수 있을 것 같은데... 
예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
“흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
“귀찮아”
그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 
주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, 
‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

입력
첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

출력
각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.

예제 입력 1  복사
3
1033 8179
1373 8017
1033 1033

예제 출력 1  복사
6
7
0
'''
from collections import deque

prime = [2, 3, 5, 7, 11, 13, 17]
check = True

for i in range(19, 10001):

    tmp = (i ** (1/2))

    for j in prime:
        if i % j == 0: 
            break

        if j > tmp or j == len(prime) - 1:
            prime.append(i) 
            break


n = int(input())

for _ in range(n):
    start, end = input().rstrip().split()

    visited = {0}

    a, b, c, d = start[0], start[1], start[2], start[3]

    q = deque()
    q.append((int(a), int(b), int(c), int(d), 0))

    visited.add(start)

    # prime: int, visited: str, q: int

    while q:

        a, b, c, d, cnt = q.popleft()

        if (a * 1000 + b * 100 + c * 10 + d) == int(end):
            check = False
            print(cnt)
            break

        for i in range(1, 11):
            a_plus_str = str((a + i) % 10) + str(b) + str(c) + str(d)
            b_plus_str = str(a) + str((b + i) % 10) + str(c) + str(d)
            c_plus_str = str(a) + str(b) + str((c + i) % 10) + str(d)
            d_plus_str = str(a) + str(b) + str(c) + str((d + i) % 10)

            if a_plus_str not in visited and int(a_plus_str) in prime and int(a_plus_str) >= 1000:
                q.append(((a + i) % 10, b, c, d, cnt + 1))
                visited.add(a_plus_str)

            if b_plus_str not in visited and int(b_plus_str) in prime:
                q.append((a, (b + i) % 10, c, d, cnt + 1))
                visited.add(b_plus_str)

            if c_plus_str not in visited and int(c_plus_str) in prime:
                q.append((a, b, (c + i) % 10, d, cnt + 1))
                visited.add(c_plus_str)
            
            if d_plus_str not in visited and int(d_plus_str) in prime:
                q.append((a, b, c, (d + i) % 10, cnt + 1))
                visited.add(d_plus_str)

if check:
    print("Impossible")

    



                