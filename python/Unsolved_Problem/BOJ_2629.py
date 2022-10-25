import sys

input = sys.stdin.readline

n_weight = int(input())
weights = list(map(int, input().split()))
n_ball = int(input())
balls = list(map(int, input().split()))

check = set()
def dp(n_arr, arr):
    if n_arr == 1:
        return set(arr)

    if tuple(sorted(arr)) in check:
        return set()
    else:
        check.add(tuple(sorted(arr)))

    ans = set(arr)
    for i in range(n_arr-1):
        for j in range(i+1, n_arr):
            ans = ans.union(dp(n_arr-1, arr[:i] + arr[i+1:j] + arr[j+1:] + [arr[i] + arr[j]]))
            ans = ans.union(dp(n_arr-1, arr[:i] + arr[i+1:j] + arr[j+1:] + [abs(arr[i] - arr[j])]))
    return ans

result = dp(n_weight, weights)

for ball in balls:
    if ball in result:
        print('Y', end=' ')
    else:
        print('N', end=' ')
