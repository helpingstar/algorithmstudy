import sys

n = int(sys.stdin.readline().rstrip())
stair = []

for _ in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))

if n > 2:
    stair_score = [0] * (n)
    stair_score[0] = stair[0]
    stair_score[1] = stair[1]
    for i in range(n-3):
        if stair_score[i+3] < stair_score[i] + stair[i+1] + stair[i+3]:
            stair_score[i+3] = stair_score[i] + stair[i+1] + stair[i+3]
        if stair_score[i+2] < stair_score[i] + stair[i+2]:
            stair_score[i+2] = stair_score[i] + stair[i+2]
    print(max((stair_score[n-1], stair_score[n-2] + stair[n-1], stair_score[n-3] + stair[n-1])))

else:
    if n == 2:
        print(stair[0] + stair[1])
    else:
        print(stair[0])