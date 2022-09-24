
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    temp1 = sum(queue1)
    temp2 = sum(queue2)
    print(temp1, temp2)
    limit = len(queue1) * 3
    if (temp1 + temp2) % 2 != 0:
        return -1
    while True:
        if temp1 > temp2:
            temp1 -= queue1[0]
            temp2 += queue1[0]
            queue2.append(queue1.popleft())
        elif temp1 < temp2:
            temp2 -= queue2[0]
            temp1 += queue2[0]
            queue1.append(queue2.popleft())
        else:  # 같을때
            return answer
        answer += 1
        if limit == answer:
            return -1