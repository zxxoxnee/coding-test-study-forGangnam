# 14502 연구소
from itertools import combinations

n, m = map(int, input().split())
array = []
for _ in range(n):
    data = list(map(int, input().split()))
    # 바이러스 찾기 , 빈칸 찾기