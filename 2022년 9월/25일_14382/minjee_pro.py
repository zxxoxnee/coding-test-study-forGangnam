# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict


def solution(fees, records):
    answer = []
    parking_in = {}
    parking_record = defaultdict(int)  # 현재까지의 total min
    result = {}  # 요금 계산한 결과

    for record in records:
        t, car, status = record.split()  # 공백열로 자르기
        if status == 'IN':
            parking_in[car] = [t]
        else:  # out
            start = parking_in[car].pop(0)
            sh, smm = start.split(':')
            eh, emm = t.split(':')
            if int(emm) >= int(smm):
                rmm = int(emm) - int(smm)
                rh = int(eh) - int(sh)
                parking_record[car] += rmm + rh * 60
            else:
                rmm = int(emm) + 60 - int(smm)
                rh = int(eh) - 1 - int(sh)
                parking_record[car] += rmm + rh * 60

    # for 문으로 parking in 돌면서 아직 남아 있는거 있으면 out 시간 23:59로 간주하고 계산하기
    for key, value in parking_in.items():
        if len(value) == 1:
            temp = value.pop(0)
            sh, smm = temp.split(':')
            rmm = 59 - int(smm)
            rh = 23 - int(sh)
            parking_record[key] += rmm + rh * 60
    # 요금계산해서 result 완성하기
    for key, value in parking_record.items():
        if value <= fees[0]:
            result[key] = fees[1]  # 기본요금
        else:
            result[key] = fees[1]  # 기본 요금
            temp = value - fees[0]
            a = temp // fees[2]
            b = temp % fees[2]
            if b == 0:
                result[key] += a * fees[3]
            else:
                result[key] += (a + 1) * fees[3]
    # answer에 오름차순으로 넣기
    for key, value in result.items():
        answer.append((key, value))
    answer.sort()
    result2 = []
    for data in answer:
        result2.append(data[1])
    return result2