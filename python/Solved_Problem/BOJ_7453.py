import sys

input = sys.stdin.readline

T = int(input())

arr = [list(map(int, input().split())) for _ in range(T)]

ab = []
cd = []
for i in range(T):
    for j in range(T):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

ab_cur = 0
cd_cur = T*T - 1

ans = 0

while ab_cur < len(ab) and 0 <= cd_cur:
    up = ab[ab_cur]
    down = cd[cd_cur]
    if up+down < 0:
        ab_cur += 1
    elif up+down > 0:
        cd_cur -= 1
    else:
        up_count = 1
        down_count = 1
        while ab_cur < T*T - 1 and ab[ab_cur] == ab[ab_cur + 1]:
            ab_cur += 1
            up_count += 1
        while  cd_cur > 0 and cd[cd_cur] == cd[cd_cur - 1]:
            cd_cur -= 1
            down_count += 1
        ab_cur += 1
        cd_cur -= 1
        ans += up_count * down_count

print(ans)
