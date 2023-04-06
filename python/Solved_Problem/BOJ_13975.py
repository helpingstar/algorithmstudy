import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    nums = list(map(int, input().split()))

    heapq.heapify(nums)
    ans = 0
    while len(nums) >= 2:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        # print(a, b)
        ans += (a + b)

        heapq.heappush(nums, a + b)

    print(ans)
