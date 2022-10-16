import sys

input = sys.stdin.readline

h, w = map(int, input().split())
board = []

for _ in range(h):
    board.append(list(map(int, list(input().rstrip()))))

# 0 > right
# 1 > down
ans = -1
for i in range(1 << (h * w)):
    i = 51
    temp_ans = 0
    check = set()
    for r in range(h):
        for c in range(w):
            if (r, c) in check:
                continue
            temp = 0
            if i >> (r * h + c) % 2 == 0: # right
                c_ = c
                while c_ < w and (i >> (r * w + c_)) % 2 == 0 and (r, c_) not in check:
                    temp = temp * 10 + board[r][c_]
                    check.add((r, c_))
                    c_ += 1
                temp_ans += temp
            else: # down
                r_ = r
                while r_ < h and (i >> (r_ * w + c)) % 2 == 1 and (r_, c) not in check:
                    temp = temp * 10 + board[r_][c]
                    check.add((r_, c))
                    r_ += 1
                temp_ans += temp

            ans = max(temp_ans, ans)

print(ans)
