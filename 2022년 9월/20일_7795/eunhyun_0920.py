'''
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. 
A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 
예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, 
B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 
8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.


두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 
둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 

출력
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.

예제 입력 1  복사
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
예제 출력 1  복사
7
1

'''

import sys

input = sys.stdin.readline

test_cnt = int(input())

for _ in range(test_cnt):
    a_cnt, b_cnt = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    a.sort()
    b.sort()

    a_pos = b_pos = 0

    while a_pos < a_cnt and b_pos < b_cnt:

        if a[a_pos] <= b[b_pos]:
            a_pos += 1
            ans += b_pos

        else:
            b_pos += 1

    if a_pos < a_cnt:
        tmp = a_cnt - a_pos
        ans += b_cnt * tmp

    #for i in range(a_pos, a_cnt):
    #   ans += b_cnt

    print(ans)



            

