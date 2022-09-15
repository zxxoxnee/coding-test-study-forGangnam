#못풀음...ㅠㅠ

import re

t = int(input())
data = []

for _ in range(t):
    d = input()
    temp = re.findall("[a-zA-Z]|\d+", d)
    data.append([d, temp])
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
