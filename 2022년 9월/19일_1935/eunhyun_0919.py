'''
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 
그리고 둘째 줄에는 후위 표기식이 주어진다. 
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 ,
5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.

예제 입력 1  복사
5
ABC*+DE/-
1
2
3
4
5
예제 출력 1  복사
6.20
A + B * C - D / E
'''
n = int(input())
post = input()

num = {}
s = 65
p = 0
stack = []

for i in range(n):
    val = int(input())
    num[s] = val
    s += 1

while p < len(post):
    if 65 <= ord(post[p]) <= 90:
        stack.append(num.get(ord(post[p])))
        
    else:
        b = stack.pop()
        a = stack.pop()

        if post[p] == "+":
            stack.append(a + b)
        elif post[p] == "-":
            stack.append(a - b)
        elif post[p] == "*":
            stack.append(a * b)
        else:
            stack.append(a / b)
    p += 1

num = stack.pop()
print(f'{num:.2f}')
