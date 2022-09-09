S = list(input())
check = False
tmp = ''
ans = ''

for i in S:
    if check == False:
        if i == "<":
            check = True
            tmp = tmp + i
        elif i == " ":
            tmp = tmp + i
            ans = ans + tmp
            tmp = ''
        # reverse
        else:
            tmp = i + tmp

    elif check == True:
        tmp = tmp + i
        if i == ">":
            check = False
            ans = ans + tmp
            tmp = ''
print(ans+tmp)