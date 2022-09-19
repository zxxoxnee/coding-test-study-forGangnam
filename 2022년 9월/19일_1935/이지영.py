N = int(input())
notaion = list(input())

ops = ["+","*","-","/"]
nums = [int(input()) for _ in range(N)]

stack = []

for n in notaion:
    if not n in ops:
        stack.append(nums[ord(n)%65])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if n == "*":
            stack.append(n1*n2)
        elif n == "+":
            stack.append(n1+n2)
        elif n == "-":
            stack.append(n1-n2)
        else:
            stack.append(n1/n2)

print(f'{stack.pop():.2f}')