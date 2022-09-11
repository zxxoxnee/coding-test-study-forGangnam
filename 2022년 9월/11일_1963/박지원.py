'''
입력으로 네 자리 소수 a, b가 주어집니다.
이제 소수 a에서 소수 b로 바꿔야 하는데, 바꿀 때의 조건은 다음과 같습니다.
숫자 중 한 자리만 바꿔야 한다.
바꾼 그 숫자도 소수여야 한다.

'에라토스테네스의 체 아이디어를 응용하자'
bfs도 사용하자

처음 들어온 숫자의 각 자릿수를 변경하면서, 소수인 경우-> 큐에 push
이미 push한 숫자-> visit 배열
자릿수를 변경해 가는 도중, 최종 목적지인 b와 같을 경우 반복문 종료 .
만약 큐가 빌 때까지 최종 목적지 b와 같았던 적이 한 번도 없을 경우, Impossible
'''

from collections import deque


def prime_nums():
    prime = [True] * 10000
    prime[0], prime[1] = False, False

    for i in range(2, 10000):
        if prime[i] == True:
            j = 2

            while i * j < 10000:
                prime[i * j] = False
                j += 1

    return prime


def bfs(start, target):
    q = deque()
    # 시작점과 카운트
    q.append([start, 0])
    visited = [False] * 10000
    visited[start] = True

    while q:
        current, cnt = q.popleft()

        if current == target:
            return cnt

        current = str(current)

        for i in range(4):
            for j in range(10):
                temp = int(current[:i] + str(j) + current[i + 1:])

                if not visited[temp] and prime_nums[temp] and temp >= 1000:
                    visited[temp] = True
                    q.append([temp, cnt + 1])
    # 불가능
    return None


if __name__ == "__main__":
    n = int(input())
    prime_nums = prime_nums()
    ans = []
    for _ in range(n):
        start, target = map(int, input().split())
        ans.append(bfs(start, target))

    for x in ans:
        if x == None:
            print("Impossible")

        else:
            print(x)