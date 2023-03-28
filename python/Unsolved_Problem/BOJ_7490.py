import sys

input = sys.stdin.readline


def solution():
    answer = []

    N = int(input())

    def dfs(value, index, string):

        if index == N:
            if value == 0:
                answer.append(string)
            return

        dfs(value+(index+1), index+1, string+'+')
        dfs(value-(index+1), index+1, string+'-')

    dfs(1, 1, '')

    print(answer)


for _ in range(int(input())):
    solution()
