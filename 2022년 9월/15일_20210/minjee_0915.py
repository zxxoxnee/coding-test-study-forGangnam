# https://www.acmicpc.net/problem/20210
n = int(input())
array = []

for _ in range(n):
    array.append(input())

# merge sort 를 이용해서 원소를 1개씩 쪼갠다음 쪼개진 원소 하나씩 조건에 맞게 비교한다
def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    merged_array = []
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    l = r = 0
    while l < len(left_array) and r < len(right_array):
        # 숫자열 vs 문자열
        if left_array[l].isdigit():
            if right_array[r].isdigit(): # 둘다 숫자열

            elif right_array[r].isalpha(): # left만 숫자
                merged_array.append(left_array[l])
                l += 1
        else: # left array[l] 가 문자열인 경우
            if right_array[r].isdigit():
                merged_array.append(right_array[r])
                r += 1
            elif right_array[r].isalpha(): # 둘다 문자열인 경우 추가 비교 필요

    return merged_array

# 결과 출력
result = merge_sort(array)
for i in result:
    print(i)