'''
3개를 마시니까.. 경우의 수
1.현재 포도주, 이전 포도주 마시고 전전 포도주는 안마시는 경우(wine[i]+wine[i-1]+d[i-3])
2.현재 포도주와 전전 포도주 마시고 이전 포도주는 마시지 않는 경우 (wine[i]+d[i-2])
3. 현대 포도주 안마시는 경우 (d[i-1])

'''
#n을 입력받는다 (포도주 잔의 개수)
n=int(input())

wine=[] #와인리스트
for i in range(n):
    wine.append(int(input()))

d=[0]*n #d는 와인을 먹은 양을 더해주는 리스트임
d[0]=wine[0] #우선 첫 원소는 동일

if n>1:
    d[1]=wine[0]+wine[1]
if n>2:
    d[2]=max(wine[2]+wine[1],wine[2]+wine[0],d[0])#wine의 첫번째+두번째, 첫번째+세번쨰, 혹은 첫 원소

for i in range(3,n+1):
    d[i] = max(d[i - 3] + wine[i - 1] + wine[i], d[i - 2] + wine[i], d[i - 1])

print(d[n])