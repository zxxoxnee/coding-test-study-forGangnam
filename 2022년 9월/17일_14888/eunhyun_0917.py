'''
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 
수식을 하나 만들 수 있다. 
이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 

예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4x5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

예제 입력 1  복사
2
5 6
0 0 1 0
예제 출력 1  복사
30
30

6
1 2 3 4 5 6
2 1 1 1
+ - * //

+ + - * //

'''

n = int(input())
arr = list(map(int, input().rstrip().split()))
o = list(map(int, input().rstrip().split()))
o_arr = []
val_max = -1000000000
val_min = 1000000000
visited = []

for i in range(4):
    for j in range(o[i]):
        if i == 0:
            o_arr.append("+")
        elif i == 1:
            o_arr.append("-")
        elif i == 2:
            o_arr.append("*")
        else:
            o_arr.append("/")
            
def find_ans(oper_pos, val_sum, arr_pos, visited):
    global arr, o_arr, val_max, val_min
    tmp_sum = 0

    if o_arr[oper_pos] == "+":
        tmp_sum = val_sum + arr[arr_pos]
    elif o_arr[oper_pos] == "-":
        tmp_sum = val_sum - arr[arr_pos]
    elif o_arr[oper_pos] == "*":
        tmp_sum = val_sum * arr[arr_pos]
    elif o_arr[oper_pos] == "/":

        if val_sum < 0:
            t_val_sum = val_sum * -1
            tmp_sum = (t_val_sum // arr[arr_pos]) * -1
        else:
            tmp_sum = val_sum // arr[arr_pos]

    if len(visited) == n-1:
        val_max = max(val_max, tmp_sum)
        val_min = min(val_min, tmp_sum)
        return

    for j in range(n-1):
        if j not in visited:
            visited.append(j)
            find_ans(j, tmp_sum, arr_pos+1, visited)
            visited.pop()


for i in range(n-1): # for operator order
    arr_pos = 0

    visited.append(i)
    find_ans(i, arr[arr_pos], arr_pos + 1, visited)
    visited.pop()

print(val_max, val_min)