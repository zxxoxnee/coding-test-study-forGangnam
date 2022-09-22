n = int(input())
graph = {}

for _ in range(n):
    node, left, right = input().split()
    graph[node] = [left, right]
# 전위 순회 root - left - right
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(graph[root][0]) # left
        preorder(graph[root][1]) # right

# 중위 순회 left - root - right
def inorder(root):
    if root != '.':
        inorder(graph[root][0])
        print(root, end='')
        inorder(graph[root][1])

# 후위 순회 left - right - root
def postorder(root): # 후위 순회
    if root != '.':
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
