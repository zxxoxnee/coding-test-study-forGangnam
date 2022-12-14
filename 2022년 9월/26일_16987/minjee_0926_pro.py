def solution(survey, choices):
    answer = ''
    n = len(choices)
    type = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    for i in range(n):
        if choices[i] == 4:
            continue
        if choices[i] < 4:
            type[survey[i][0]] += score[choices[i]]
        if choices[i] > 4:
            type[survey[i][1]] += score[choices[i]]
    print(type)
    if type['R'] >= type['T']:
        answer += 'R'
    else:
        answer += 'T'

    if type['C'] >= type['F']:
        answer += 'C'
    else:
        answer += 'F'

    if type['J'] >= type['M']:
        answer += 'J'
    else:
        answer += 'M'

    if type['A'] >= type['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer