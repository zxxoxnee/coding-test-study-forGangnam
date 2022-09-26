def solution(survey, choices):
    answer = ''
    score = [-1,3,2,1,0,1,2,3]
    result = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    indicators = [["R","T"],["C","F"],["J","M"],["A","N"]]
    
    for i in range(len(survey)):
        print(survey[i],choices[i])
        if choices[i] == 4:
            continue
        elif choices[i]<4:
            result[survey[i][0]]+=score[choices[i]]
        else:
            result[survey[i][1]]+=score[choices[i]]
    
    for i in indicators:
        if result[i[0]] < result[i[1]]:
            answer+=i[1]
        else:
            answer+=i[0]
        
    return answer