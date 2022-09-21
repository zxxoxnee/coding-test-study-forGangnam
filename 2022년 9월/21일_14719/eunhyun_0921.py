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

left, right =0, len(a) - 1
lp, rp = 1, right - 1
l_count, r_count = 0, 0

while left < right:
    if a[left] <= a[right]:
        if a[left] - a[lp] > 0:
            l_count += a[left] - a[lp]
            lp += 1
        else:
            left = lp
            lp += 1
    else:
        if a[right] - a[rp] > 0:
            r_count += a[right] - a[rp]
            rp -= 1
        else:
            right = rp
            rp -= 1
        
print(l_count + r_count)