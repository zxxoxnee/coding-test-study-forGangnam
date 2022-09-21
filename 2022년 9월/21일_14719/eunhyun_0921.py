'''
입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.

예제 입력 1  복사
4 4
3 0 1 4
예제 출력 1  복사
5



'''

b = input()
a = list(map(int, input().split()))

ans = 0
left, right =0, len(a)-1
left_max, right_max = a[left], a[right]

while left<right:
    left_max, right_max = max(a[left], left_max), max(a[right], right_max)

    if left_max <= right_max:
        ans += left_max - a[left]
        left += 1
    else:
        ans += right_max - a[right]
        right -= 1

print(ans)


