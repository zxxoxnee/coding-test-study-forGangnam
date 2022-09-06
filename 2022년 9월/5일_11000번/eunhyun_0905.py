'''
시간: 1초, 메모리제한: 256MB

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 
최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. 
(즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)


입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 10^9)

출력
강의실의 개수를 출력하라.

예제 입력 1  복사
3
1 3
2 4
3 5
예제 출력 1  복사
2


1 
'''
import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

q = []
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    if q[0] > arr[i][0]:
        heapq.heappush(q, arr[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, arr[i][1])

print(len(q))
