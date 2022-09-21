import sys

n = int(sys.stdin.readline())

#노드, 왼쪽 자식 노드, 오른쪽 자식 노드
# 루트 > 왼자식 > 오자식 순

class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


def preorder(node) : # node > 왼 > 오
    print(node.data,end='')
    if node.left != '.' : preorder(node.left)
    if node.right != '.' : preorder(node.right)

def inorder(node) : # 왼 > node > 오
    if node.left != '.' : inorder(node.left)
    print(node.data,end='')
    if node.right != '.' : inorder(node.right)

def postorder(node) : # 왼 > 오 > node
    if node.left != '.' : postorder(node.left)
    if node.right != '.' : postorder(node.right)
    print(node.data,end='')

tree = []
for _ in range(n) :
    i = sys.stdin.readline().split()
    node = Node(i[0])
    node.left = i[1]
    node.right = i[2]
    tree.append(node)
# print(tree)

#트리 이스트들의 부모 노드와 자식 노드들을 서로 매칭시켜 트리 구성
for i in range(n) :
    for j in range(n) :
        if tree[i].data == tree[j].left : tree[j].left = tree[i]
        elif tree[i].data == tree[j].right : tree[j].right = tree[i]

# print(tree[].left)
preorder(tree[0]) 
print()
inorder(tree[0])
print()
postorder(tree[0])