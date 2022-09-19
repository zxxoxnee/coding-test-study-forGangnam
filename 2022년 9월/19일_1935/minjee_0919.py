# python에서 A가 아스키코드 65

n = int(input()) # 피연산자 개수
data = input()
num = []
for _ in range(n):
    num.append(int(input()))

stack = []
result = 0

for i in data:
    if i.isalpha():
        stack.append(num[ord(i)-65]) # 숫자면 스택에 쌓는다
    else:
        if i == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(y*x)
        elif i == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(y/x)
        elif i == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(y+x)
        elif i == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y-x)
result = stack.pop()

# 소수점 둘째자리까지 출력하기 - 포멧 함수를 사용한다
print("{:.2f}".format(result))