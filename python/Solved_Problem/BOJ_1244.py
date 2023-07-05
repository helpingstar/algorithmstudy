import sys


def solution():
    input = sys.stdin.readline

    n_switch = int(input())
    switches = list(map(int, input().split()))

    n_stud = int(input())
    students = [list(map(int, input().split())) for _ in range(n_stud)]
    # 남자 : 1 / 여자 : 2

    for g, n in students:
        if g == 1:
            for i in range(n, n_switch+1, n):
                switches[i-1] ^= 1
        else:
            n -= 1
            switches[n] ^= 1
            c = 1
            while (n - c >= 0) and (n + c < n_switch) and (switches[n-c] == switches[n+c]):
                switches[n-c] ^= 1
                switches[n+c] ^= 1
                c += 1

    for i in range(0, n_switch, 20):
        print(*switches[i:i+20])


if __name__ == "__main__":
    solution()
