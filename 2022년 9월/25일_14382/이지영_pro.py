import math
from datetime import datetime

def solution(fees, records):
    dictionary = {}
    result_dictionary = {}
    for record in records:
        record = record.split()
        if record[1] in dictionary.keys():
            dictionary[record[1]].append(record[0])
        else:
            dictionary[record[1]]=[record[0]]

    for key in dictionary.keys():
        if len(dictionary[key])%2 !=0:
            dictionary[key].append('23:59')
        result = datetime.strptime("00:00","%H:%M")
        while dictionary[key]:
            OUT = datetime.strptime(dictionary[key].pop(),"%H:%M")
            IN = datetime.strptime(dictionary[key].pop(),"%H:%M")
            result += OUT-IN
        total = result.hour*60+result.minute
        if total < fees[0]:
            result_dictionary[key] = fees[1]
        else:
            total = total - fees[0]
            total = math.ceil(total / fees[2])
            result_dictionary[key] = fees[1]+total*fees[3]
    result = []
    
    for i,j in sorted(result_dictionary.items()):
        result.append(j)
    return result