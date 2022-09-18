# 2212 센서
n = int(input()) # sensor 개수
k = int(input()) # 집중국 개수
sensor = list(map(int, input().split()))

if n <= k:
    print(0)
else:
    sensor.sort()
    distance = [] # 각 센서끼리의 거리의 차를 저장하는 배열
    for i in range(n-1):
        distance.append(sensor[i+1]-sensor[i])
    distance.sort(reverse=True)
    # 가장 큰 값 k-1 개를 뺀
    print(sum(distance[k-1:]))

