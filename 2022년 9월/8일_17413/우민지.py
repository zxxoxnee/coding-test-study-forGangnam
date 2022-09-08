# Boj 17413
s = list(input())
s += ' ' # 마지막 eof 처리
i = 0

while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1 # '>' 만난 경우 한 칸 이동
    elif s[i].isalnum(): # 문자열 & 숫자
        start = i
        while s[i].isalnum() and i < len(s):
            i += 1
        temp = s[start:i]
        temp.reverse()
        s[start:i] = temp
    else: # 공백
        i += 1 # 공백열은 한 칸 이동

print("".join(s))
