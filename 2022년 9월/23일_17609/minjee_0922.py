n = int(input())

def solve(left, right):
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            # 오른쪽 문자열 제거
            if left < right -1:
                temp = word[:right] + word[right+1:]
                if temp[:] == temp[::-1]:
                    return 1
            # 왼쪽 문자열 제거
            if left + 1 < right:
                temp = word[:left] + word[left+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(n):
    word = input()
    left = 0
    right = len(word) - 1
    print(solve(left, right))


