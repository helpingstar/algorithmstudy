# BOJ 1038

def add_digit(digit,num):    #자리수에 따라 증가
    if digit==1:
        decreasing.append(num)
    else:
        for i in range(num%10):
            add_digit(digit-1,num*10+i)

def backtracking(digit):    #백트래킹 시작
    # digit-1 부터 시작하는 이유 : digit은 자릿수인데
    # 자릿수의 맨 왼쪽 숫자는 자릿수 - 1 보다 작을 수 없으므로
    for i in range(digit-1,10):
        add_digit(digit,i)
    
decreasing=[]        #감소하는 숫자 리스트

# i : 자릿수
for i in range(1,11):
    backtracking(i)

n=int(input())
if n>=len(decreasing):        #감소하는 숫자가 없을 때
    print(-1)
else:
    print(decreasing[n])