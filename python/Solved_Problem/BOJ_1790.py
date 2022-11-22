import sys

input = sys.stdin.readline

n, k = map(int, input().split())

count = 1
cum = 0
prev = 0
while True:
    cum += 9 * (10**(count-1)) * count
    if k <= cum:
        break
    count += 1
    prev = cum

k_temp = k - prev -1

quo = k_temp // count
mod = k_temp % count

# print(quo)
# print(mod)

num = 10**(count-1) + quo

if n < num:
    print(-1)
else:
    print(str(num)[mod])
