import sys
import bisect

input = sys.stdin.readline

N, H = map(int, input().split())

bottom = []
top = []
for i in range(N):
    temp = int(input())
    if i & 1 == 1:
        bottom.append(temp)
    else:
        top.append(temp)

bottom.sort()
top.sort()

# print(f'[debug] top : {top}')
# print(f'[debug] bottom : {bottom}')


n_hurdle = sys.maxsize
cnt = 0

for i in range(1, H+1):
    h_bottom = i
    h_top = H - i + 1

    c_top = N//2 - bisect.bisect_left(top, h_top)
    c_bottom = N//2 - bisect.bisect_left(bottom, h_bottom)

    # print(f'[debug] c_top: {c_top}')
    # print(f'[debug] c_bottom: {c_bottom}')
    

    total = c_top + c_bottom
    # print(f'[debug] {total}')
    if total < n_hurdle:
        n_hurdle = total
        cnt = 1
    elif total == n_hurdle:
        cnt += 1

print(n_hurdle, cnt)