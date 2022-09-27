# programmers https://school.programmers.co.kr/learn/courses/30/lessons/92342

from collections import deque


def solution(n, info):
    answer = []
    queue = deque([0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])  # count, arrow
    max_gap = 0  # 라이언 - 어피치 점수 최대 차

    while queue:
        count, arrow = queue.popleft()
        if arrow == n:  # while 문 종료
            ryan, apeach = 0, 0  # 라이언 어피치 점수 계산
            for i in range(11):
                if arrow[i] > info[i]:  # 라이언이 이김
                    ryan += 10 - i
                else:
                    apeach += 10 - i
                if ryan > apeach:
                    gap = ryan - apeach
                    if max_gap >= gap:
                        continue
                    else:
                        max_gap = gap
                        answer = []
                    answer.append(arrow)  # 화살 기록 저장하기
        # 화살 쏘기




