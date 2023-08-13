import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    def cal(a, b, o):
        if o == "+":
            return a + b
        else:
            return a - b

    def dp(cnt):
        nonlocal C, op_list
        if cnt == C:
            prev = 0
            now = 1
            op = '+'
            for i in range(C):
                if op_list[i] == ' ':
                    now = now * 10 + (i+2)
                else:
                    prev = cal(prev, now, op)
                    op = op_list[i]
                    now = i+2
            result = cal(prev, now, op)
            if result == 0:
                print(1, end='')
                for i in range(C):
                    print(f"{op_list[i]}{i+2}", end='')
                print()
            return

        for o in (" ", "+", "-"):
            op_list[cnt] = o
            dp(cnt+1)

    for _ in range(N):
        C = int(input())
        C -= 1
        op_list = [' '] * C
        dp(0)
        print()


solution()
