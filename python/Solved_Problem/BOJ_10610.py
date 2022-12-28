import sys

input = sys.stdin.readline

nums = list(map(int, list(input().rstrip())))

num_list = [0] * 10

for num in nums:
    num_list[num] += 1

if sum(nums) % 3 != 0 or num_list[0] == 0:
    print(-1)
else:
    ans = ''
    for i in range(9, -1, -1):
        ans += str(i) * num_list[i]
    print(ans)
