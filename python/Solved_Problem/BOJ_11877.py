import sys

input = sys.stdin.readline

def solution():
    n, target = map(int, input().split())
    if target > (n-1) * (n-2) // 2:
        return [-1]
    if n <= 2:
        if target == 0:
            return [1, 2]
        else:
            return [-1]
    used = []
    for i in range(1, n-1):
        if (n-1 - i) <= target:
            target -= (n-1 - i)
            used.append(i)
            if target == 0:
                break
    ans = [n] + used + [n-1]
    used = set(used)
    for i in range(n-2, 0, -1):
        if i not in used:
            ans.append(i)
    return ans

print(*solution())
