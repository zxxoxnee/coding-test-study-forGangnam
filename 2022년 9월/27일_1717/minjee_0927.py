# 1717 백준
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n+1)]

def find_parents(a):
    if parents[a] != a: # 자기 자신이 root 노드가 아닌경우 다시 find 연산 수행하기
        parents[a] = find_parents(parents[a])
    return parents[a]

def union(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a # 루트 노드가 값이 작은 것이 상위라고 가정하기
    else:
        parents[a] = b

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 합치기
        union(a, b)
    else: # 동일 집합인지 판단
        if find_parents(a) == find_parents(b):
            print('YES')
        else:
            print('NO')
