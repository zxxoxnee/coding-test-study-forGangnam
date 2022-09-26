'''
먼저, 숫자 N을 뽑는다. 그리고 N, 2 × N, 3 × N 등을 떠올린다. 숫자를 떠올릴 때 마다, 그 숫자의 모든 자리수의 숫자들을 적어놓는데, 
이미 적은 숫자는 또 적지 않는다. 0에서 9까지의 모든 숫자가 적히게 되면 잠이 든다.

블리트릭스는 N에서 시작해서 i × N 후에는 (i + 1) × N을 떠올리게 된다. 예를 들어 N = 1692 일 경우, 다음 과 같이 진행된다:

N = 1692. 1, 2, 6, 9가 기록된다.
2N = 3384. 1, 2, 3, 4, 6, 8, 9가 기록된다.
3N = 5076. 모든 수가 기록되고, 잠에 빠진다.
블리트릭스가 잠에 빠지는 수는 무엇인가? 영원히 잠에 들 수 없다면 INSOMNIA라고 출력하라.

입력
첫 번째 행은 케이스의 개수, T이다. 다음 행부터는 T개의 케이스들이 나온다. 각 케이스는 블리트릭스가 고른 하나의 숫자 N으로 구성된다.

제한

1 ≤ T ≤ 100.
0 ≤ N ≤ 106.
출력
각 케이스에 대해서, 케이스 번호가 x이고 y가 정답일 때, Case #x: y라고 출력해야 한다.

2 4 6 8 10 12 14 16 18 20 22 24 26 28
예제 입력 1  복사
5
0
1
2
11
1692

예제 출력 1  복사
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076
'''

def solution(cnt):
    arr = [0] * (10)

    n = int(input())

    if n == 0:
        print(f"Case #{cnt + 1}: INSOMNIA")
        return
    
    p = 1

    while sum(arr) < 10:
        tmp = n * p
        s = str(tmp)

        for i in range(len(s)):
            if arr[int(s[i])] == 0:
                arr[int(s[i])] = 1

        p += 1

    print(f"Case #{cnt + 1}: {(p-1) * n}")

    return



if __name__ == "__main__":
    t = int(input())

    for cnt in range(t):
        solution(cnt)
