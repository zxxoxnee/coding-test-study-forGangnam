# programmers https://school.programmers.co.kr/learn/courses/30/lessons/92342
from collections import deque
import copy

def bfs(n, info):
    answer = []
    queue = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])  # count, arrow
    max_gap = 0  # 라이언 - 어피치 점수 최대 차

    while queue:
        count, arrow = queue.popleft()
        if sum(arrow) == n:  # while 문 종료
            ryan = 0
            apeach = 0 # 라이언 어피치 점수 계산
            for i in range(11):
                if not (arrow[i] == 0 and info[i] == 0):
                    if arrow[i] > info[i]:  # 라이언이 이김
                        ryan += 10 - i
                    else:
                        apeach += 10 - i
            if ryan > apeach:
                gap = ryan - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap
                    answer.clear()
                answer.append(arrow)  # 화살 기록 저장하기

        elif sum(arrow) > n: # 화살 더 쏜 경우
            continue
        elif count == 10:
            temp = arrow.copy()
            temp[count] = n - sum(temp)
            queue.append((-1, temp))
        else:
            temp = arrow.copy()
            temp[count] = info[count]+1 # 화살 쏘는 경우 무조건 어피치보다 +1 많이 쏴야 득점
            queue.append((count+1, temp))
            temp2 = arrow.copy()
            temp2[count] = 0 # 안쏘는 경우
            queue.append((count+1, temp2))
    return answer


def solution(n, info):
    result = bfs(n, info)
    if not result:
        return [-1]
    elif len(result) == 1: # case가 하나밖에 없을 때
        return result[0]
    else: # 과녘 점수 작은것들을 최대한 많이 포함하는 경우 (bfs에서 인덱스 오름차순으로 돌리기 때문에 뒤에 가있)
        return result[-1]
