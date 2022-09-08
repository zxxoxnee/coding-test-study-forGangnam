s = input()
result = ''
tag = []
w = []
i = 0

while i < len(s):
    if s[i] == "<":
        while True:
            tag.append(s[i])
            i += 1
            if s[i] == ">":
                tag.append(s[i])
                break
        result += "".join(tag)
        i = i+1
        tag = []
    elif s[i] == ' ':
        result += ' '
        i +=1
    else:
        while True:
            w.append(s[i])
            i += 1
            if i>=len(s) or s[i]==' ' or s[i] =="<": ##인덱스 체크랑 리스트 요소 비교시 인텍스 체크 먼저 안그러면 인덱스 에러남
                result += "".join(reversed(w))
                w = []
                break
print(result)