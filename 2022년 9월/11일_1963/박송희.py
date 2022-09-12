from collections import deque
import sys
sys.stdin = open("20220911_1963_소수찾기.txt", "r")

#1부터 9999까지 소수를 먼저 찾는다
def isPrime(n) :
    board = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(3, n+1) :
        if board[i] == True :
            primes.append(i)

        for j in range(i*2, n+1, i) :
            board[j] = False
    return primes

#소수인 경우 큐에 넣는다, 큐에 있는 4자리의 숫자는 각각 자리수 마다 0~9까지 바꾼다
#바꾼 수가 소수인 경우 다시 큐에 넣는다.
def BFS(start, target) :
    dq = deque()
    dq.append([start, 0])

    visited = [False] * (10000)
    visited[start] = True

    while dq :
        nowValue, count = dq.popleft()

        #각 자리수를 하나씩 뽑고 0부터 9까지 교체해보자
        strValue = list(str(nowValue))        #자리수 교체를 위해 문자열 -> 리스트 처리

        #목표 숫자에 도달하면 중지
        if nowValue == target :
            return count

        #[0][1][2][3] <-- 각 자리수에 0~9까지를 다 넣어본다. 
        for i in range(4) :
            copyValue = strValue[::]          #원본 숫자 유지를 위해 복사
            for j in range(10) :
                copyValue[i] = str(j)
                findValue = int("".join(copyValue))

                #기존에 만들지 않았었고, 1000보다 크고, 만든 숫자가 소수인 경우에 큐에 다시 넣기
                if visited[findValue] == False and 1000 <= findValue and findValue in primesList :
                    visited[findValue] = True
                    dq.append([findValue, count+1])

n = int(input())
primesList = isPrime(10000)

for i in range(n) :
    start, target = map(int, input().split())

    result = BFS(start, target)

    if result != None :
        print(result)
    else :
        print("Impossible")

# 우선 네 자리 수인 9999까지의 모든 수를 완전탐색을 통해서 소수인지 판별을 한다.
# 각 자리수마다 숫자(0 ~ 9)를 바꾸어 가며 소수인 수는 큐에 넣어서 또 다시 자릿수를 바꾸어 가며 바꾸어야 하는 숫자가 나올 때 판별한다.
# 큐에 넣은 숫자는 방문 처리를 한다. (visited) - 카운트 중복 방지
# 과정 중에는 네 자리 숫자를 유지해야 하므로 바꾼 숫자가 1000이상인지 확인한다.