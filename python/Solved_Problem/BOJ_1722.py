import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    f_list = [1] * N
    for i in range(2, N):
        f_list[i] = f_list[i - 1] * i

    questions = list(map(int, input().split()))
    num_list = [i for i in range(1, N + 1)]
    if questions[0] == 1:
        ans = []
        num = questions[1]
        for cnt in range(N - 1, -1, -1):
            quo = (num - 1) // f_list[cnt]
            ans.append(num_list.pop(quo))
            num -= f_list[cnt] * quo
            cnt -= 1
        print(*ans)
    else:
        ans = 1
        for i in range(1, N + 1):
            num = questions[i]
            n_fac = f_list[-i]
            idx = num_list.index(num)
            ans += n_fac * idx
            num_list.pop(idx)
        print(ans)


solution()
