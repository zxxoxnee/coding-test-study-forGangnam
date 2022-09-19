# 후위표기식을 중위표기식으로 잘못이해
n = int(input())
alpha = []
op = []
data = {}
for i in range(65,91):
    data[chr(i)] = 0
# print(data)
for i in input():
    if i.isalpha():
        alpha.append(i)
    else:
        op.append(i)
for i in range(n):
    data[chr(i+65)] = int(input())
# print(data)
# print(alpha)
# print(op)
res = data[alpha[0]]

for i in range(len(op)):
    if op[i] == '+':
        res += data[alpha[i+1]]
    elif op[i] == '-':
        res -= data[alpha[i+1]]
    elif op[i] == '*':
        res *= data[alpha[i+1]]
    else:
        res /= data[alpha[i+1]]
print(res)