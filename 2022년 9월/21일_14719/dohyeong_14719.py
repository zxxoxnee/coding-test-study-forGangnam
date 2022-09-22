h,w = map(int, input().split())

data = list(map(int, input().split()))

volume = 0
left, right = 0, len(data) - 1
left_max, right_max = data[left], data[right]

while left < right:
    left_max, right_max = max(data[left], left_max), max(data[right], right_max)

    if left_max <= right_max:
        volume += left_max - data[left]
        left += 1
    else:
        volume += right_max-data[right]
        right -= 1
print(volume)