import sys

def solution():
    input = sys.stdin.readline

    temp = input().split()
    num = int(temp[0])

    n_list = temp[1:]

    while num > len(n_list):
        temp = input().split()
        n_list.extend(temp)
    
    n_list = list(map(lambda x: int(x[::-1]), n_list))
    n_list.sort()
    print(*n_list, sep='\n')

solution()