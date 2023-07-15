import sys

input = sys.stdin.readline


def get_shortcut(sen, shortcuts: set):
    splitted_sen = sen.split()
    for i, word in enumerate(splitted_sen):
        if word[0].lower() not in shortcuts:
            shortcuts.add(word[0].lower())
            result = []
            if i > 0:
                result.append(' '.join(splitted_sen[:i]))
            result.append(f'[{word[0]}]{splitted_sen[i][1:]}')
            if i < len(splitted_sen):
                result.append(' '.join(splitted_sen[i+1:]))
            return ' '.join(result)
    for i, c in enumerate(sen):
        if c == ' ':
            continue
        if c.lower() not in shortcuts:
            shortcuts.add(c.lower())
            return f'{sen[:i]}[{c}]{sen[i+1:]}'
    return sen


def solution():
    n = int(input())
    shortcuts = set()
    for _ in range(n):
        sen = input().rstrip()
        print(get_shortcut(sen, shortcuts))


solution()
