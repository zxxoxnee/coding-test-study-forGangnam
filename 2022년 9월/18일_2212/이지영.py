N= int(input())
K= int(input())

sensor = list(map(int,input().split()))

sensor.sort()
if K>=N:
    print(0)
else:
    dist = []

    for i in range(N-1):
        dist.append(sensor[i+1]-sensor[i])

    dist.sort(reverse=True)

    for i in range(K-1):
        dist.pop(0)

    print(sum(dist))
