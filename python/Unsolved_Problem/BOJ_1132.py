import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    n_table = [[0] * 12 for _ in range(10)]
    first = set()
    all_chars = set()
    for _ in range(N):
        word = input().rstrip()
        first.add(ord(word[0]) - ord('A'))
        w_len = len(word)
        for i, c in enumerate(word):
            n_table[ord(c) - ord('A')][w_len - 1 - i] += 1
            all_chars.add(c)
    all_number = []
    # 문자 선택
    for c in range(10):
        # 어떤 숫자
        for i in range(10):
            if c in first and i == 0:
                continue
            num = 0
            for idx, n in enumerate(n_table[c]):
                num += (10 ** idx) * n * i
            all_number.append((num, i, c))
    all_number.sort(reverse=True, key=lambda x: x[0])
    result = 0
    num_visited = [False] * 10
    char_visited = [False] * 10
    num_count = 0
    for num, i, c in all_number:
        if num_visited[i]:
            continue
        if char_visited[c]:
            continue
        print(num, i, c)
        result += num
        num_visited[i] = True
        char_visited[c] = True
        num_count += 1
        if num_count == len(all_chars):
            break

    print(result)
    return

solution()
