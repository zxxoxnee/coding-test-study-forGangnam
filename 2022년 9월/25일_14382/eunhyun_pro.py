import math

def solution(fees, records):
    answer = []
    car_info = {}

    for i in records:
        hour, minute = map(int, i[:5].split(":"))
        number = i[6:10]
        status = i[11:]

        if number in car_info:
            tmp = car_info.get(number)
            tmp.append([hour, minute, status])
            car_info[number] = tmp
    
        else:
            car_info[number] = [[hour, minute, status]]

    sort_car_info = sorted(car_info)
    
    for i in sort_car_info:
        val = car_info.get(i)
        stack = []
        amount = 0
        for j in range(len(val)):
            if val[j][2] == "IN":
                stack.append((val[j][0], val[j][1]))
            else:
                hour, minute = stack.pop()

                ans_hour = (val[j][0] - hour) * 60
                ans_minute = (val[j][1] - minute)
                amount += (ans_hour + ans_minute)

        if stack:
            hour, minute = stack.pop()

            ans_hour = (23 - hour) * 60
            ans_minute = (59 - minute)

            amount += (ans_hour + ans_minute)
        
        if amount >= fees[0]:
            answer.append(fees[1] + math.ceil((amount - fees[0]) / fees[2] ) * fees[3])
        else:
            answer.append(fees[1])
            
            

    print(answer)
    return answer