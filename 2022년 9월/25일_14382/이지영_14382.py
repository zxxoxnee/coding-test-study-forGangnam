T = int(input())

for t in range(T):
    n = int(input())
    if n == 0:
        print(f'Case #{t+1}: INSOMNIA')
        continue
    i = 1
    nums = [0,1,2,3,4,5,6,7,8,9]
    while True:
        tmp = list(str(n*i))
        while tmp:
            temp = int(tmp.pop())
            if temp in nums:
                nums.pop(nums.index(temp))
        if not nums:
            print(f'Case #{t+1}: {n*i}')
            break
        else:
            i+=1