# 14382
t = int(input())

for i in range(t):
    check = {}
    n = int(input())
    now = n
    if n == 0:
        print('Case #'+str(i+1)+": INSOMNIA")
    else:
        count = 1
        while True:
            temp = str(now)
            for j in temp:
                if int(j) not in check:
                    check[j] = 1
                else:
                    continue
            if sum(check.values()) == 10:
                print("Case #"+str(i+1)+ ": "+str(now)) # , 로 하면 공백열이 생겨버리므로 + 를 이용해서 문자열을 만들어야 함
                break
            count += 1
            now = n * count
