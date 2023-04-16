import sys

input = sys.stdin.readline

N = int(input())

num_list = [input().rstrip() for _ in range(N)]

def sum_num(word):
    temp = 0
    for c in word:
        if c.isdigit():
            temp += int(c)
    return temp

num_list.sort(key=lambda x: (len(x), sum_num(x), x))

print(*num_list, sep='\n')
