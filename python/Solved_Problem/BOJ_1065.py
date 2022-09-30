import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    if N < 100:
        return N
    ans = 99
    for i in range(100, N+1):
        flag = True
        temp = list(map(int, list(str(i))))
        diff = temp[0] - temp[1]
        for j in range(len(temp)-2):
            if temp[j+1] - temp[j+2] != diff:
                flag = False
                break
        if flag:
            ans += 1
    return ans

print(solution())
