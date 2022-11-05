import sys

input = sys.stdin.readline

n_weight = int(input())
weight_list = list(map(int, input().split()))
n_ball = int(input())
ball_list = list(map(int, input().split()))

check = set()
num_list = set()

def dp(arr, num):
    # print(f'[debug] arr: {arr}, num: {num}')
    num_list.add(num)

    if not arr:
        return
    if (tuple(sorted(arr)), num) in check:
        return
    check.add((tuple(sorted(arr)), num))
    dp(arr[1:], abs(num-arr[0]))
    dp(arr[1:], num+arr[0])
    dp(arr[1:], num)

dp(weight_list, 0)

for ball in ball_list:
    print('Y' if ball in num_list else 'N', end=' ')
