h, w = map(int, input().split())
block = list(map(int, input().split()))
volume = 0
stack = []
for i in range(w):
    stack.append(i) # index
    if block[stack[-1]] < block[i]:
        height = stack.pop()
        volume += block[]



print(volume)