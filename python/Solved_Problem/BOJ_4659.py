import sys

input = sys.stdin.readline


def check(word):
    aeiou = {'a', 'e', 'i', 'o', 'u'}
    has_aeiou = False
    n_mo = 0
    n_ja = 0
    for i, c in enumerate(word):
        if c in aeiou:
            has_aeiou = True

        if c in aeiou:
            n_mo += 1
            n_ja = 0
        else:
            n_mo = 0
            n_ja += 1

        if n_mo == 3 or n_ja == 3:
            return False

        if (i > 0) and (c == word[i-1]) and c not in {'e', 'o'}:
            return False

    return has_aeiou


while True:
    word = input().rstrip()

    if word == 'end':
        break

    if check(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
