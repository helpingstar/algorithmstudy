"""
해당 규칙대로 나열된 수들은 트리를 위에서 아래로 정사영 한 모양과 같다.
= 배열을 2분으로 쪼개기 시작할 때 그 중앙은 그 배열을 포함한 Tree의 Root다
다이나믹 프로그래밍으로 좌측부 우측부를 나눠서 재귀하면 된다.
"""

import sys
input = sys.stdin.readline

k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k+1)]


def get_k(cnt, l, r):

    mid = (l+r) // 2
    if k == 1:
        tree[1].append(arr[0])
        return
    if cnt == k-1:
        tree[cnt+1].append(arr[l])
        tree[cnt].append(arr[mid]) # 여기서 mid == l+1
        tree[cnt+1].append(arr[r])
    else:
        tree[cnt].append(arr[(l+r) // 2])
        get_k(cnt+1, l, mid-1) # 좌측부
        get_k(cnt+1, mid+1, r) # 우측부

get_k(1, 0, len(arr) - 1)

for row in tree[1:]:
    print(*row, sep=' ')