import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    chars = dict()
    for _ in range(N):
        word = input().rstrip()
        L = len(word)
        for i, c in enumerate(word):
            if c not in chars:
                chars[c] = [0] * (50)
            chars[c][L-1-i] += 1
    K = int(input())
    numbers = []
    for k in chars.keys():
        if k.isdigit():
            num = int(k)
        else:
            num = ord(k) - ord('A') + 10
        origin = 0
        z_num = 0
        norm = 1
        for n in chars[k]:
            origin += num * n * norm
            z_num += 35 * n * norm
            norm *= 36
        numbers.append((z_num - origin, origin, z_num))
    numbers.sort(key=lambda x: (-x[0], -x[1]))
    result = 0
    for diff, o, z in numbers:
        if K > 0:
            result += z
            K -= 1
        else:
            result += o

    ans = ''
    to36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while result > 0:
        ans = to36[result % 36] + ans
        result //= 36
    if ans == '':
        print(0)
    else:
        print(ans)

solution()
