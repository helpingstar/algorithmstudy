import sys

input = sys.stdin.readline


def solution():
    n, x = map(int, input().split())
    # 최대로 넣을 수 있는 물의 양 : (n-1)(n-2) // 2
    if x > ((n-1) * (n-2)) // 2:
        return [-1]
    # (n)과 (n-1)사이에 넣을 그래프, 이 안에서 모두 해결 가능
    is_used = [False] * (n-1)
    # 기준 그래프(물이 이 이상으로 불가)
    top = n-1
    ans = []
    for i in range(1, n-1):
        if x >= (top - i):
            # 그리디, 물의 최대양부터 넣어서(작은 그래프) 물의 양을 줄인다.
            is_used[i] = True
            ans.append(i)
            # 물을 넣으면 타겟값을 줄인다.
            x -= (top -i)
            # 타겟이 만족되면 break, 이것은 무조건 호출된다.
            if x == 0:
                break
    # 넣은 값들을 n, n-1 사이에 배치한다.
    ans = [n] + ans + [n-1]
    # 나머지 값들을 내림차순으로 배열하여 물을 받지 못하게 한다.
    for i in range(n-2, 0, -1):
        if not is_used[i]:
            ans.append(i)
    return ans

print(*solution())
