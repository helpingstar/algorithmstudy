import sys

input = sys.stdin.readline
is_valid = True

word = input().rstrip()


def dp(open, cur):
    global word
    global is_valid
    o_cur = cur
    print(
        f'[OPEN ] TRUE  cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
    if not is_valid:
        print(f'[CLOSE] FALSE cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
        return 0, 0


    result = 0
    while True:
        if word[cur] == '(':
            d_result, d_cur = dp('(', cur+1)
            result += d_result * 2
            cur += d_cur
        elif word[cur] == '[':
            d_result, d_cur = dp('[', cur+1)
            result += d_result * 3
            cur += d_cur
        elif word[cur] == ')':
            if open == '(':
                print(f'[CLOSE] TRUE  cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
                return max(1, result), cur - o_cur + 2
            else:
                print(f'[CLOSE] FALSE cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
                is_valid = False
                return 0, 0
        else:  # ']'
            if open == '[':
                print(f'[CLOSE] TRUE  cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
                return max(1, result), cur - o_cur + 2
            else:
                print(f'[CLOSE] FALSE cur: {cur}, open: {open}, cur - o_cur : {cur - o_cur}')
                is_valid = False
                return 0, 0
        cur += 1


print(dp(None, 0))
print(is_valid)
