'''

20210

Windows의 파일 탐색기를 보면 파일이 정렬된 방식이 보통의 정렬 방식과는 다른 것을 알 수 있다.

보통 문자열을 정렬할 때는 맨 앞부터 한 글자씩 비교하다가 
어느 한쪽이 끝나거나 일치하지 않는 글자가 있으면 그 위치의 문자를 비교한 결과가 문자열 전체를 비교한 결과가 된다. 

한편 파일 탐색기는 여러 자리의 수를 한 글자로 취급해서 비교하는데, 
이 때문에 "str12ing"과 "str123ing" 중 후자가 아니라 전자가 앞에 온다. 
이러한 정렬 방식을 종종 "natural sort"라고 하기도 한다.

여러 개의 문자열이 주어지면 natural sort 방식으로 정렬한 결과를 출력하는 프로그램을 작성해 보자. 
이 문제에서 구현할 알고리즘은 다음을 만족해야 한다.

    1. 문자열은 알파벳 대소문자와 숫자로만 이루어져 있다.
    2. 숫자열이 알파벳보다 앞에 오고, 알파벳끼리는 AaBbCc...XxYyZz의 순서를 따른다.
    3. 문자열을 비교하는 중 숫자가 있을 경우 그 다음에 오는 숫자를 최대한 많이 묶어 한 단위로 비교한다. 
       예를 들어 "a12bc345"는 "a", "12", "b", "c", "345"의 다섯 단위로 이루어져 있다.
    4. 숫자열끼리는 십진법으로 읽어서 더 작은 것이 앞에 온다. 이때 예제 2에서와 같이 값이 2^63을 초과할 수 있다.
    5. 같은 값을 가지는 숫자열일 경우 앞에 따라붙는 0의 개수가 적은 것이 앞에 온다.
    
입력
첫 줄에 문자열의 개수 N(2 ≤ N ≤ 10,000)이 주어진다. 그 다음 N줄에 정렬할 문자열이 한 줄에 하나씩 주어진다.

모든 문자열의 길이는 100 이하이며, 알파벳 대소문자와 숫자로만 이루어져 있다.

출력
N줄에 걸쳐 문제에서 설명한 대로 문자열을 정렬한 결과를 출력한다.

예제 입력 1  복사
8
Foo1Bar
Foo12Bar
Foo3bar
Fo6Bar
Foo00012Bar
Foo3Bar
foo4bar
FOOBAR

예제 출력 1  복사
FOOBAR
Fo6Bar
Foo1Bar
Foo3Bar
Foo3bar
Foo12Bar
Foo00012Bar
foo4bar
'''

import heapq
import re

n = int(input())
s_sort = []
ans = []
word_priority = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8 , '9': 9, 'A': 10, 'a': 11, 'B': 12,

'b': 13, 'C': 14, 'c': 15, 'D': 16, 'd': 17, 'E': 18, 'e': 19, 'F': 20, 'f': 21, 'G': 22, 'g': 23, 'H': 24, 'h': 25, 'I': 26,
'i': 27, 'J': 28, 'j': 29, 'K': 30, 'k': 31, 'L': 32, 'l': 33, 'N': 34, 'n': 35, 'M': 36, 'm': 37, 'O': 38, 'o': 39, 'P': 40,
'p': 41, 'Q': 42, 'q': 43, 'R': 44, 'r': 45, 'S': 46, 's': 47, 'T': 48, 't': 49, 'U': 50, 'u': 51, 'V': 52, 'v': 53, 'W': 54,
'w': 55, 'X': 56, 'x': 57, 'Y': 58, 'y': 59, 'Z': 60, 'z': 61}

for _ in range(n):
    s = input()
    tmp_str = re.finditer("[A-z]", s)
    tmp_num = re.findall("[0-9]+",s)

    ex_x, ex_y = 0, len(s)
    tmp_ans = []

    if len(tmp_num) >= 1 and len(tmp_num[0]) == len(s):
        tmp_ans.append(s[:])

    else:
        for i in tmp_str:
            x, y = i.span()

            if ex_x < x:
                tmp_ans.append(s[ex_x:x])
                ex_x = x

            if x == ex_x:
                print(s[x:y])
                tmp_ans.append(s[x:y])
                ex_x = y

        if s[-1] != tmp_ans[-1][-1]:
            tmp_ans.append(s[ex_x:])

    tmp_ans.append(s)
    s_sort.append(tmp_ans)

s_sort()

for i in range(len(s_sort)):
    tmp = []
    for j in range(len(s_sort[i])):
        if s_sort[i][j].isdigit():
            pass






'''
while d < n - 1:

    if s_sort[d][0] != s_sort[d+1][0]:
        if s_sort[d][0].isdigit() and s_sort[d+1][0].isdigit():
            tmp_sort = []
            heapq.heappush(tmp_sort, [int(s_sort[d][0]), len(s_sort[d][0]), s_sort[d][-1]])
            d += 1

            while s_sort[d][0].isdigit():
                heapq.heappush(tmp_sort, [int(s_sort[d][0]), len(s_sort[d][0]), s_sort[d][-1]])
                d += 1
                if d >= n:
                    break
                while tmp_sort:
                    val = heapq.heappop(tmp_sort)
                    ans.append(val[-1])
        else:
            ans.append(s_sort[d][-1])
            d += 1

    else:
        first_val = s_sort[d][0]
        end = d 
        tmp_sort = []
        final_sort = []
        
        while first_val == s_sort[end][0]:
            tmp_sort.append(s_sort[end])
            end += 1
            if end >= n:
                break

        for i in range(len(tmp_sort)):
            for j in range(len(tmp_sort[i])-1):
                if tmp_sort[i][j].isdigit():
                    tmp_sort[i][j] = (int(tmp_sort[i][j]), len(tmp_sort[i][j]))
    
        tmp_sort.sort()

        for i in tmp_sort:
            ans.append(i[-1])

        d = end

if len(ans) != n:
    ans.append(s_sort[-1][-1])

for i in ans:
    print(i)
'''
''' 
1. 처음 저장할떄 문자/숫자 구분해서 저장
2. 그상태로 정렬
3. 전체 돌면서 재 정렬
    1_ 첫 요소와 다음 요소가 다르다
        => 그 다음 요소의 첫 요소가 숫자라면 첫 요소가 숫자가 아닌 곳 까지 내려가기, 찾았다면 정렬하기
        => 문자라면 word append 하고 p를 정렬 된 마지막 자리로 지정
    
    2_ 첫번쨰 요소와 그 다음 자리의 첫번째 요소가 같다.
        => 밑으로 요소가 다른 곳 까지 찾는다.
        => 구해진 리스트를 돌면서 가로로 요소가 다른 곳 까지 찾는다.
            + 길이가 다른곳
            + 값이 다르다
'''