T = int(input())

def get_release(num:int)->int:
    answer = num
    check = [True for _ in range(num+1)]
    for i in range(2, num+1):
        for j in range(i, num+1, i):
            if check[j]:
                answer -= 1
                check[j] = False
            else:
                answer += 1
                check[j] = True
    return answer

for _ in range(T):
    print(get_release(int(input())))
