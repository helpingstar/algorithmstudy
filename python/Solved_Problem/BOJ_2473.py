import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()
def solution():
    n_close = sys.maxsize
    close_list = []

    for i in range(n-2):
        l, r = i+1, n-1
        while l < r:
            temp = arr[i] + arr[l] + arr[r]
            if abs(temp) < n_close:
                n_close = abs(temp)
                close_list = [arr[i], arr[l], arr[r]]
            if n_close == 0:
                return close_list
            if temp < 0:
                l += 1
            else:
                r -= 1

    return close_list

print(*solution())
