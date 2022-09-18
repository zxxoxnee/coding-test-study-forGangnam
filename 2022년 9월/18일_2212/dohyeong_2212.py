n = int(input())
k = int(input())

data = list(map(int, input().split()))
data.sort()
temp = []
for i in range(len(data)-1):
    temp.append(data[i+1] - data[i])
temp.sort()
# print(temp)
print(sum(temp[:n-k]))