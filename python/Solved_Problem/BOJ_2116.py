import sys

input = sys.stdin.readline


def solution():
    counter = (5, 3, 4, 1, 2, 0)
    n_dice = int(input())
    dices = [tuple(map(int, input().split())) for _ in range(n_dice)]

    def get_max(a, b):
        if b > a:
            a, b = b, a

        if a == 6:
            if b == 5:
                return 4
            else:
                return 5
        else:
            return 6

    ans = 0
    for i in range(6):
        result = 0
        prev_pos = i
        prev_num = dices[0][prev_pos]
        prev_counter_pos = counter[prev_pos]
        prev_counter_number = dices[0][prev_counter_pos]
        result += get_max(prev_num, prev_counter_number)
        for i in range(1, n_dice):
            now_number = prev_counter_number
            now_number_pos = dices[i].index(now_number)
            now_counter_pos = counter[now_number_pos]
            now_counter_number = dices[i][now_counter_pos]
            result += get_max(now_number, now_counter_number)

            prev_counter_number = now_counter_number
        ans = max(ans, result)
    print(ans)


solution()
