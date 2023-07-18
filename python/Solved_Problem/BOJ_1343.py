import sys

input = sys.stdin.readline

def solution():
    word = input().rstrip().split('.')
    result = ''
    for w in word:
        if (len(w) % 4) % 2 == 1:
            return -1
        else:
            if len(w) % 4 == 2:
                result += ('AAAA' * (len(w) // 4) + 'BB')
            else:
                result += ('AAAA' * (len(w) // 4))
        result += '.'
    return result[:-1]

print(solution())
