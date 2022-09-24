# 카카오 2018 - 두 큐 합 같게 만들기


알고리즘
kakao
두
큐
합
같게
만들기
Python
2022.
9.
24.
01: 56
수정삭제공개

https: // school.programmers.co.kr / learn / courses / 30 / lessons / 118667

프로그래머스

코드
중심의
개발자
채용.스택
기반의
포지션
매칭.프로그래머스의
개발자
맞춤형
프로필을
등록하고, 나와
기술
궁합이
잘
맞는
기업들을
매칭
받으세요.

programmers.co.kr
리스트로
두고
풀어도
될것같긴한데
나는
popleft()
연산을
쓰고
싶어서
deque으로
자료구조를
사용했다
그런데
while 문 탈출조건인 limit에 대해서 고민이 좀 많았다;;

그리고
카카오의
공식
해설에
따르면
투포인터로도
풀
수
있다..
https: // tech.kakao.com / 2022 / 07 / 13 / 2022 - coding - test - summer - internship /  #:~:text=%EB%AC%B8%EC%A0%9C%202%EB%B2%88%20%E2%80%93%20%EB%91%90%20%ED%81%90%20%ED%95%A9%20%EA%B0%99%EA%B2%8C%20%EB%A7%8C%EB%93%A4%EA%B8%B0&text=%EC%B2%98%EC%9D%8C%20%EC%A3%BC%EC%96%B4%EC%A7%84%20queue1%EC%9D%98%20%ED%95%A9,%EB%A5%BC%20queue2%EB%A1%9C%20%EB%84%98%EA%B2%A8%EC%A4%8D%EB%8B%88%EB%8B%A4.

2022
테크
여름인턴십
코딩테스트
해설

2022
년
카카오
여름
인턴십
코딩
테스트가
지난
5
월
7
일에
5
시간에
걸쳐
진행되었습니다.시간이
부족하여
문제를
풀지
못하는
아쉬움이
없도록
1
시간을
늘려
테스트를
진행한
것이
작년과
조금

tech.kakao.com
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