def solution(queue1, queue2):
    answer = 0
    
    one_sum = sum(queue1)
    two_sum = sum(queue2)
    
    val = one_sum + two_sum
    
    if val % 2 != 0:
        return -1
    
    q1 = q2 = 0
    cnt= 0
    point_break = len(queue1) * 3
    
    while True:
        
        if one_sum > (val // 2):
            queue2.append(queue1[q1])
            two_sum += queue1[q1]
            one_sum -= queue1[q1]
            q1 += 1
            answer += 1
            
        elif two_sum > (val // 2):
            queue1.append(queue2[q2])
            one_sum += queue2[q2]
            two_sum -= queue2[q2]
            q2 += 1
            answer += 1
        
        if answer > point_break:
            return -1
        
        if one_sum == (val // 2) and two_sum == (val//2):
            break
            
    return answer

n = list(map(int, input().split()))
m = list(map(int, input().split()))

print(solution(n, m))
