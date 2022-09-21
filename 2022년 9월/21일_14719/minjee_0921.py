h, w = map(int, input().split())
block = list(map(int, input().split()))
volume = 0

for i in range(1, w-1):
    # 자기 자신의 높이보다 좌/우에 높은 것이 있는지 확인
    left = max(block[:i])
    right = max(block[i+1:])
    height = min(left, right) # 둘 중에 작은 값이 기준이 된다
    volume += height - block[i]

print(volume)