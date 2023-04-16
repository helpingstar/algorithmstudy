import sys

input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,l,m = map(int, input().split())

fish = []
answer = 0
for _ in range(m):
    x,y = map(int, input().split())
    fish.append((x-1,y-1))
def solv():
    for sx,sy in fish:
        for l1 in range(1,l//2):
            l2 = l//2-l1
            move_net(sx-l1, sy-l2, l1, l2)
    print(answer)

def move_net(sx,sy,l1,l2):
    global answer
    d = 0
    l1_cnt, l2_cnt = l1, l2
    while d != 4:
        if d in [1, 3]:
            sx += dx[d]
            l1_cnt -= 1
            if l1_cnt == 0:
                l1_cnt = l1
                d += 1
        else:
            sy += dy[d]
            l2_cnt -= 1
            if l2_cnt == 0:
                l2_cnt = l2
                d += 1
        if sx >= 0 and sy >= 0:
            ex = sx + l1 + 1
            ey = sy + l2 + 1
            answer = max(answer, count_fish(sx, sy, ex, ey))

def count_fish(sx,sy,ex,ey):
    cnt = 0
    if ex > n or ey > n:
        return 0
    for x,y in fish:
        if sx <= x < ex and sy <= y < ey:
            cnt += 1
    return cnt

solv()
