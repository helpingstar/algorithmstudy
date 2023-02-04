import sys

input = sys.stdin.readline

a, b = map(int ,input().split())

def get_one(num):
    if num <= 2:
        return num
    elif num == 3:
        return 4
    bnum = bin(num)[2:]
    len_num = len(bnum)
    temp = 0
    result = 0
    # print(f'[debug]  {bnum, len_num}')
    for i in range(len_num-1):
        if bnum[i] == '1':
            fac = len_num - i
            result += temp * (2 ** (fac-1)) + (2 ** (fac-2)) * (fac-1)
            temp += 1
    if bnum[-1] == '1':
        result += temp + 1
    result += temp
    return result

print(get_one(b) - get_one(a-1))
