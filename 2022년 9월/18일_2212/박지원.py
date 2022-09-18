'''

문제 이해가 안되는ㄷㅔ ;;
-> k개의 집중국으로 모든 센서를 커버할 수 있도록 하는 각 집중국 범위의 합 구하라는거낟
집중국 k의 개수가 n보다 같거나 크면 0


1. 입력받기
2. k>=n 0 출력, 종료
3. 센서의 길이 오름차순 정렬
4. 센서 거리 차이를 담은 배열 생성
5. 차이 배열을 내림차순으로 정렬
6. 차이 배열의 k-1 ~마지막까지 합 출력


'''

import sys

n=int(input())
k=int(input())
sensor=list(map(int,input().split()))
sensor.sort()

array=[]
for i in range(0,n-1):
    array.append(sensor[i+1]-sensor[i])

array.sort()

print(sum(array[:n-k]))