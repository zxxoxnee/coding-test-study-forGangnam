# 3085

def check(board):
    n=len(board)
    result=1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        count=1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
        	# 이전 것과 같다면 count에 1 더하기
                count += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                count=1
                
            # 비교해서 현재 count가 더 크다면 result 갱신하기
            if count > result:
                result = count

        # 행 순회하면서 연속되는 숫자 세기
        count=1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
        	# 이전 것과 같다면 count에 1 더하기
                count += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                count=1
                
            # 비교해서 현재 count가 더 크다면 result 갱신하기
            if count > result:
                result = count

    return result

n=int(input())
board=[list(input()) for _ in range(n)]
result=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인접한 것과 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            # check는 boardd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=check(board)
