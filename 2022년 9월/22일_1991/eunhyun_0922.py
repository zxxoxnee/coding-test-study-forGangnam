'''
입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1  복사
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1  복사
ABDCEFG
DBAECFG
DBEGFCA
'''

n = int(input())
t = {}
ans1 = ""
ans2 = ""
ans3 = ""

for _ in range(n):
    pa, left_child, right_child = input().split()
    t[pa] = [left_child, right_child]

def preorder(val):
    global ans1

    if val in t:
        tmp = t.get(val)
    else:
        return
 
    t_l = tmp[0]
    t_r = tmp[1]

    ans1 += val
    preorder(t_l)
    preorder(t_r)


def inorder(val):
    global ans2

    if val in t:
        tmp = t.get(val)
    else:
        return

    t_l = tmp[0]
    t_r = tmp[1]

    inorder(t_l)
    ans2 += val
    inorder(t_r)

def postorder(val):
    global ans3
    
    if val in t:
        tmp = t.get(val)
    else:
        return

    t_l = tmp[0]
    t_r = tmp[1]

    postorder(t_l)
    postorder(t_r)
    ans3 += val


preorder('A')
inorder('A')
postorder('A')

print(ans1)
print(ans2)
print(ans3)