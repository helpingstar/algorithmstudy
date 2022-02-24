import sys

input = sys.stdin.readline

n = int(input())
w_list = list(map(int, input().split()))

l, r = 0, n-1

answer = sys.maxsize
min_lr = [l, r]

while l < r:
    if abs(w_list[l] + w_list[r]) < answer:
        answer = abs(w_list[l] + w_list[r])
        min_lr = [l, r]
    
    if w_list[l] + w_list[r] < 0:
        l += 1
    else:
        r -= 1

print(w_list[min_lr[0]], w_list[min_lr[1]])