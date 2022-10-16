t = int(input())

def solution():
    h, w, n = map(int ,input().split())
    if h == 1:
        return f'1{n:02d}'
    if w == 1:
        return f'{n}01'
    return f'{(n-1) % h + 1}{(n-1) // h + 1:02d}'

for _ in range(t):
    print(solution())
