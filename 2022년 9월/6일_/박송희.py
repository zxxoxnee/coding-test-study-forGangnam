import sys
sys.stdin = open("20220906_타임어택_백준_16953_A_B.txt", "r")
from collections import deque
start, end = map(int, input().split())
dq = deque()
dq.append([start, 1])        #시작값과 카운트의 초기 값을 넣어준다.
result = []                 #결과를 저장할 목록

#큐가 빌때까지!
while dq :
    nowValue, nowCount = dq.popleft()

    #목표치(end) 값과 같은 경우 카운트를 넣어준다
    if nowValue == end :
        result.append(nowCount)
        break

    #2를 곱한게 end보다 작은 경우만 큐에 넣어준다
    if nowValue * 2 <= end  :
        dq.append([nowValue * 2, nowCount + 1])
    
    #1을 수의 가장 오른쪽에 추가가 end보다 작은 경우만 큐에 넣어준다
    if int(str(nowValue) + '1') <= end :
        dq.append([int(str(nowValue) + '1'), nowCount + 1])

if len(result) > 0 :
    print(min(result))      #end값을 만든 카운트를 저장해준다.
else :
    print(-1)

#2 162
#2 → 4 → 8 → 81 → 162

#정수 A를 B로 변경
#가능한 연산은 2개
#2곱하기
#1을 오른쪽에 추가
#연산의 최소 횟수

#만들수없는 경우 -1