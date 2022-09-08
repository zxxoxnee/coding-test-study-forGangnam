import sys
# sys.stdin = open("20220830_타임어택_백준_17413_단어뒤짚기2.txt", "r")

line = sys.stdin.readline()
answer = ''

stack = []
wordStack = []
idx = 0

for i in range(len(line)) :
  #<인 경우 스택에 넣기
  if line[i] == "<" :
    stack.append(line[i])

    #다음에 <가 들어온 경우 wordStack에 있는거 다 빼줌
    if 0 < len(wordStack) : 
      transeWod = "".join(wordStack)[::-1]
      answer += transeWod
      wordStack = []
      continue

  #>가 들어온 경우 stack에 있는거 다 뽑아주기
  if line[i] == ">" :
    stack.append(line[i])
    answer += "".join(stack)
    stack = []
    continue

  #스택에 값이 있으면 죄다 < > 로 감싸진 정보
  if len(stack) > 0 :
    stack.append(line[i])
    continue

  #위에까지 처리하면 stack이 아래부터는 비어있다.
  if len(wordStack) > 0 :
    #인덱스 끝인 경우
    if i == len(line) - 1 : 
      wordStack.append(line[i])     #공백도 추가하고 스택에 넣기
      transeWod = "".join(wordStack)[::-1]
      answer += transeWod
      wordStack = []
      continue

    #공백인 경우
    if line[i] == " " : 
      transeWod = "".join(wordStack)[::-1]
      transeWod += ' '              #공백은 뒤에 추가
      answer += transeWod
      wordStack = []
      continue

  #스택이 빈 경우 단어 추가
  if len(stack) == 0 :
    wordStack.append(line[i])

#출력형식 오류로 한줄 없애주기
print(answer.replace("\n", ""));