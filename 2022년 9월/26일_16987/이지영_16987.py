N = int(input())

eggs = []


for _ in range(N):
    t1, t2 = map(int, input().split())
    eggs.append([t1,t2])

answer = 0

def breakEgg(idx,eggs):
    global answer
    if idx==N:
        count = 0
        for e in eggs:
            if e[0] <= 0:
                count+=1
        answer = max(answer,count)
        return 

    if eggs[idx][0]<=0:
        breakEgg(idx+1,eggs)
    else:
        allBreak = True
        for i in range(len(eggs)):
            if idx != i and eggs[i][0] > 0:
                allBreak= False
                eggs[idx][0] -= eggs[i][-1]
                eggs[i][0] -= eggs[idx][-1]
                breakEgg(idx+1,eggs)
                eggs[idx][0] += eggs[i][-1]
                eggs[i][0] += eggs[idx][-1]
        if allBreak:
            breakEgg(N,eggs)
breakEgg(0,eggs)
print(answer)