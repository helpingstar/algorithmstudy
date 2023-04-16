import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    nums.sort(key=lambda x: x[0])

    ans = 0
    n_min = sys.maxsize
    for i in range(N):
        if n_min > nums[i][1]:
            ans += 1
            n_min = nums[i][1]
    print(ans)

for _ in range(int(input())):
    solution()
