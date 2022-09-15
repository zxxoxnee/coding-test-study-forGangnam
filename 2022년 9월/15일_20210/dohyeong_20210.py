import re
n = int(input())
data = []
for _ in range(n):
    d = input()
    d = re.findall("[a-zA-Z]|\d+", d)
    data.append(d)
print(data)