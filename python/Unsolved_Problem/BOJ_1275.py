import sys

input = sys.stdin.readline
from collections import deque


n_number, n_turn = map(int, input().split())

nums = [0] + list(map(int, input().split()))

def get_sum(left, right):
    result = 0
    q = deque()
    q.append((1, len(nums)))
    while q:
        nleft, nright = q.popleft()

        print(f'[debug]  nleft: {nleft}, nright: {nright}')
        nmid = (nleft + nright) // 2
        if nright < left or right < nleft:
            continue

        if left <= nleft and nright <= right:
            result += sum(nums[nleft:nright+1])
        else:
            q.append((nleft, nmid))
            q.append((nmid+1, nright))
    return result

for _ in range(n_turn):
    x, y, a, b = map(int, input().split())
    print(get_sum(x, y))
    nums[a] = b
