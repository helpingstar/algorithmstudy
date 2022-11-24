import sys

input = sys.stdin.readline

n = int(input())


def solution():
    water = list(map(int, input().split()))
    have_plus=False
    have_minus=False
    for i in water:
        if i < 0:
            have_minus = True
        elif i > 0:
            have_plus = True

    if have_plus and not have_minus:
        return water[0], water[1]
    if not have_plus and have_minus:
        return water[-2], water[-1]

    ans = [-1, -1]
    min_ans = sys.maxsize
    left, right = 0, n-1
    while left < right:
        if water[left] + water[right] == 0:
            return [water[left], water[right]]
        elif water[left] + water[right] > 0:
            if abs(water[left] + water[right]) < min_ans:
                ans = [water[left], water[right]]
                min_ans = abs(water[left] + water[right])
            right -= 1
        else:
            if abs(water[left] + water[right]) < min_ans:
                ans = [water[left], water[right]]
                min_ans = abs(water[left] + water[right])
            left += 1
    return ans

print(*solution())
