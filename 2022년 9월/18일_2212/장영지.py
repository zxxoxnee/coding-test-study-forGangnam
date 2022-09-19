import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
spot = list(map(int, sys.stdin.readline().split()))

spot = list(set(spot))
spot.sort()
print(spot)