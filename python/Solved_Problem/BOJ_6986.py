import sys

input = sys.stdin.readline

N, K = map(int, input().split())


def round(x):
    x *= 100
    if x - int(x) >= 0.5:
        x = int(x) + 1
    else:
        x = int(x)

    return x/100


nums = [float(input()) for _ in range(N)]

nums.sort()

print(f'{round(sum(nums[K:N-K]) / (N-2*K)):.02f}')
print(f'{round((sum(nums[K:N-K]) + (nums[K] + nums[N-K-1])*K) / N):.02f}')
