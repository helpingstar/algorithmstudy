import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = []

zero = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        zero += 1
        continue
    arr.append(num)

arr.sort()

arr = deque(arr)

def solution(arr: deque, zero:int):
    ans = 0
    if len(arr) == 1:
        if arr[0] < 0 and zero > 0:
            return 0
        else:
            return arr[0]
    # n > 0, 2
    while len(arr) >= 2 and arr[-1] > 1 and arr[-2] > 1:
        a = arr.pop()
        b = arr.pop()
        ans += a * b
    # n < 0, 2
    while len(arr) >= 2 and arr[0] < 0 and arr[1] < 0:
        a = arr.popleft()
        b = arr.popleft()
        ans += a * b
    if arr:
        if arr[0] == -1:
            if zero > 0:
                arr.popleft()
            else:
                ans -= 1
                arr.popleft()
    while arr:
        ans += arr.pop()
    
    return ans
        
print(solution(arr, zero))