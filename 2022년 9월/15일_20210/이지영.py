N = int(input())
strings = [input() for _ in range(N)]
dex = ['1','2','3','4','5','6','7','8','0','9']
arr = [[] for _ in range(100)]
maxlen = -1
result = []
stand = []
## 문자열 쪼개기, 숫자는 하나로 묶었음
for s in strings:
    s = list(s)
    tmp = []
    idx = 0
    while s:
        if s[0].isdigit():
            t= ''
            while s and s[0].isdigit():
                t+=s.pop(0)
            arr[idx].append(t)
            idx+=1
        else:
            arr[idx].append(s.pop(0))
            idx +=1
    maxlen = max(idx,maxlen)
    arr.append(tmp)
arr = arr[:maxlen]
idx = 0
for a in range(len(arr)):
    s = list(set(arr[a]))
    n = len(s)
    for i in range(n-1):
        for j in range(n-i-1):
            if s[j].isdigit() and s[j+1].isdigit():
                if int(s[j]) == int(s[j+1]):
                    if len(s[j+1]) < len(s[j]):
                        s[j],s[j+1] = s[j+1],s[j]
                elif int(s[j+1]) < int(s[j]):
                    s[j],s[j+1] = s[j+1],s[j]
            elif s[j+1].isdigit():
                s[j],s[j+1] = s[j+1],s[j]
            else:
                if s[j].upper() == s[j+1].upper():
                    if s[j+1]<s[j]:
                        s[j],s[j+1] = s[j+1],s[j]
                elif s[j+1].upper() < s[j].upper():
                    s[j],s[j+1] = s[j+1],s[j]
    s.reverse()

### 한글자씩 하면 될거 같았는데,, 안된다,,

# # print(stand)    
# print(arr)
print(result)