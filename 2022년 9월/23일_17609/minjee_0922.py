n = int(input())
for _ in range(n):
    word = input()
    left = 0
    right = len(word) -1
    similar = 0
    check = 0 # ababbabaa 이런 케이스 검증용
    c_similar = 0
    while left <= right:
        print(left, right)
        print(word[left], word[right])
        if word[left] == word[right]:
            left += 1
            right -= 1
            print("=====")
        else:
            if word[left+1] == word[right] and word[left] == word[right-1]:
                # 왼쪽 땡기는 방법
                if check == 0:
                    i = left + 1
                    j = right
                    check += 1 # 왼쪽 땡기는거 체크했다는 뜻임
                    while i <= j:
                        if word[i] == word[j]:
                            i += 1
                            j -= 1
                        else:
                            if word[i+1] == word[j]:
                                i += 1
                                j -= 1
                            else:
                                if word[i + 1] == word[j]:
                                    i += 1
                                    c_similar += 1
                                elif word[i] == word[j + 1]:
                                    j += 1
                                    c_similar += 1
                                else:
                                    c_similar += 2
                                    break

                if check == 1: # 오른쪽 땡기는거 검사할 차
                    i = left
                    j = right - 1
                    while i <= j:
                        if word[i] == word[j]:
                            i += 1
                            j -= 1
                        else:
                            if word[i+1] == word[j]:
                                i += 1
                                c_similar += 1
                            elif word[i] == word[j+1]:
                                j += 1
                                c_similar += 1
                            else:
                                c_similar += 2
                                break


            if check == 1: #이미 검사함
                break
            elif word[left+1] == word[right]:
                print("llll")
                left += 1
                similar += 1
            elif word[left] == word[right-1]:
                print("rrrrr")
                right -= 1
                similar += 1
            else: # 다른 경우
                similar += 2
                print("hhh")
                break
    if check == 0: # 특이 케이스 없는 경우
        if similar >= 2:
            print(2)
        else:
            print(similar)
    else:
        if c_similar == 0:
            print(1)
        else:
            print(2)
