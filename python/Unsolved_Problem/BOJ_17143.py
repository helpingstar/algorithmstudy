import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())


def move(x, y, vel, way, big):
    global r
    global c
    if way in {3, 4}:
        r_velocity = (y-1 + vel) % c
        way_change = (y-1 + vel) // c

        if (y == 1) or (way == 3 and y != c):
            # way_change: 홀수 : 유지
            if way_change % 2 != 0:
                n_y = c - 1 - r_velocity
                n_way = 4
            else:
                n_y = r_velocity
                n_way = 3
        else:
            if way_change % 2 != 0:
                n_y = r_velocity
                n_way = 3
            else:
                n_y = c - 1 - r_velocity
                n_way = 4
        
        return x, n_y + 1, vel, n_way, big

    else:

        c_velocity = (x-1 + vel) % r
        way_change = (x-1 + vel) % r

        if (x == 1) or (way == 2 and x != r):
            if way_change % 2 != 0:
                n_x = r - 1 - c_velocity
                n_way = 1
            else:
                n_x = c_velocity
                n_way = 2
        else:
            if way_change % 2 != 0:
                n_x = c_velocity
                n_way = 2
            else:
                n_x = r - 1 - c_velocity
                n_way = 1

        return n_x +1 , y, vel, n_way, big

for _ in range(m):
    x, y, vel, way, big = map(int, input().split())
    print(*move(x, y, vel, way, big))