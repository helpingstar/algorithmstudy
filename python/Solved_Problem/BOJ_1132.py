import sys

input = sys.stdin.readline

def solution():

    N = int(input())
    n_table = [[0] * 12 for _ in range(10)]
    is_first = [0] * 10
    for _ in range(N):
        word = input().rstrip()
        is_first[ord(word[0]) - ord('A')] = 1
        L = len(word)
        for i, c in enumerate(word):
            n_table[ord(c) - ord('A')][L-1-i] += 1

    num_list = []
    for i in range(10):
        result = 0
        for j in range(12):
            result += (10 ** j) * n_table[i][j]
        num_list.append((result, is_first[i]))
    num_list.sort(key=lambda x: (-x[1], -x[0]))
    # print(num_list)
    num_list.pop()
    num_list.sort(key=lambda x: x[0])
    ans = 0
    for i in range(9):
        ans += (i+1) * num_list[i][0]
    print(ans)


solution()
