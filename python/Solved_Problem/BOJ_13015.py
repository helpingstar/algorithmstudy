import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    print(f'{"*"*N}{" "*(2*N-3)}{"*"*N}')
    for i in range(N-2):
        print(f'{" "*(i+1)}*{" "*(N-2)}*{" "*(2*N-3-(2*(i+1)))}*{" "*(N-2)}*')
    print(f'{" "*(N-1)}*{" "*(N-2)}*{" "*(N-2)}*')
    for i in reversed(range(N-2)):
        print(f'{" "*(i+1)}*{" "*(N-2)}*{" "*(2*N-3-(2*(i+1)))}*{" "*(N-2)}*')
    print(f'{"*"*N}{" "*(2*N-3)}{"*"*N}')


solution()
