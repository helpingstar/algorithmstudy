import sys

input = sys.stdin.readline

T = int(input())


def hs2s(hs):
    h, s = map(int, hs.split(':'))
    return h * 60 + s


def s2hs(s):
    return f'{s // 60:02d}:{s % 60:02d}'


goals = []

for _ in range(T):
    a, b = input().split()
    goals.append((int(a), b))

score = [0, 0]
winning_time = [0, 0]
prev_time = 0

status = 0

for team, time in goals:
    if status == 1:
        winning_time[0] += hs2s(time) - prev_time
    elif status == 2:
        winning_time[1] += hs2s(time) - prev_time

    score[team-1] += 1
    if score[0] > score[1]:
        status = 1
    elif score[0] < score[1]:
        status = 2
    else:
        status = 0

    prev_time = hs2s(time)

if status == 1:
    winning_time[0] += hs2s('48:00') - prev_time
elif status == 2:
    winning_time[1] += hs2s('48:00') - prev_time

print(s2hs(winning_time[0]))
print(s2hs(winning_time[1]))
