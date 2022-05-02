import sys

input = sys.stdin.readline

l, c = map(int, input().split())
chars = input().split()

chars.sort()

def add_pwd(length, pwd):
    if length == l:
        con = 0
        vow = 0
        for v in pwd:
            if chars[v] in 'aeiou':
                vow += 1
            else:
                con += 1
        if vow >= 1 and con >= 2:
            word = ''
            for i in pwd:
                word += chars[i]
            print(word)
    else:
        # c - (l - length) 이상은 어차피 안되므로 생략한다.
        for i in range(pwd[-1] + 1, c - (l - length) + 1):
            add_pwd(length + 1, pwd + [i])

for i in range(c - l + 1):
    add_pwd(1, [i])
