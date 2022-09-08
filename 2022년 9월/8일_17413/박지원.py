'''

문자열에서 단어만 뒤집을 것.

'<'와 '>' 사이에는 알파벳 소문자와 공백만 있다.
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고,
연속하는 두 단어는 공백 하나로 구분한다.
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

문제푸는 아이디어
s가 공백으로 구분되어있다면 <>안에 있ㄴ는 게 아닌 이상 temp에 넣어주기.

1. 만약 문자열이 <일 경우, >를 만날때까지 그대로 res리스트에 넣어주기
2. 만약 문자열이 공백일 경우, 처음이 아닐 경우, res에 넣어주기
3. 문자열이 알파벳일 경우 공백이나 <를 만날 때까지 temp에 넣어주고 reverse해서 res에 넣어주기

1,2,3반복 (문자열이 끝날때까지)
'''
temp=[]
word=[]
res=''
i=0
#문자열을  입력받기
str=input()


while i < len(str):
    if str[i] == "<":
        while True:
            word.append(str[i])
            i+=1
            if str[i]==">":
                word.append(str[i])
                i += 1
                break
        res+="".join(word)
        word=[] #초기화
    elif str[i] == ' ' and i != 0:
        res+=' '
        i+=1
    else:
        while True:
            temp.append(str[i])
            i+=1
            if i>=len(str) or str[i]==' ' or str[i]=="<":
                res+="".join(reversed(temp))
                temp=[] #초기화
                break


print(res)