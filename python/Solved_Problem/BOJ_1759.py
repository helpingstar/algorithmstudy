import sys

input = sys.stdin.readline

l, c = map(int, input().split())
words = list(input().split())

ja = []
mo = []

ans = []

# n_ja 남은 필요 자음
# n_mo 남은 필요 모음
def dp(word, arr, n_ja, n_mo, count, div):
    if (n_ja + n_mo) > count:
        return
    if count == 0:
        ans.append(''.join(sorted(word)))
    else:
        for i in range(div, len(arr)):
            if arr[i] in 'aeiou':
                dp(word + arr[i], arr[:i] + arr[i+1:], n_ja, max(0, n_mo-1), count-1, i)
            else:
                dp(word + arr[i], arr[:i] + arr[i+1:], max(0, n_ja-1), n_mo, count-1, i)

dp('', words, 2, 1, l, 0)
ans.sort()
print(*ans, sep='\n')
