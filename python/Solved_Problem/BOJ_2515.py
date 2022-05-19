"""
배열을 사용하여 bottom-up 방식을 사용하려다가 시간초과로 실패하여
이분탐색 방법으로 하게 되었다.
"""

import sys
import bisect

input = sys.stdin.readline

# (9, 3)
n, s = map(int, input().split())
pics = [(0, 0)]

for _ in range(n):
    a, b = map(int, input().split())
    pics.append((a, b))

pics.sort()

# pics : [(0, 0), (8, 230), (10, 100), (15, 80), (17, 200), (20, 75) ... ]

max_num = [0] * (n+1)

# max_num : [0, 0, 0, 0, 0, 0 ... ]

for i in range(1, n+1):
    # pics의 높이가 s보다 낮으면 continue한다.
    if pics[i][0] < s:
        continue
    # i번째의 그림 크기 - s에서 취할 수 있는 가장 큰 수를 구하기 위한 prev를 구한다.
    # 예를 들어 pics[3] - s (15 - 3)의 bisect_right는 3이고 1을 빼면 해당 max의 index가 나온다
    # 위의 경우 bisect_right(pics, (pics[i][0]) - s, 1001) 은 3이 나올것이고 1을 빼면 2가 나오는데
    # 이는 10까지의 최대 가격이다. (10~15사이는 없으므로 10을 취해도 된다)

    # 두번째 인자로 1001을 넣은 이유는 cost가 최대 1000이기 때문이다.
    # bisect.bisect_right를 한 이유는 같은 height가 있을 경우 정렬시 큰 cost는 오른쪽에 가기 때문에
    # 오른쪽 bisect_right를 한 후 1을 빼면 동일 height중 가장 큰 cost를 취급할 수 있기 때문이다.
    prev = bisect.bisect_right(pics, (pics[i][0] - s, 1001)) - 1
    # 그전 것을 그대로 계승할 것인지, 자신 + (자신 - s)까지의 최댓값을 취할 것인지를 선택한다.
    max_num[i] = max(max_num[i-1], pics[i][1] + max_num[prev])


print(max_num[n])