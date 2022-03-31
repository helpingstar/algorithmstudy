from os import sep
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def get_result(cmds, len, nums):
    if cmds.count('D') > len:
        return 'error'
    q = deque(nums)
    reversed = False
    for cmd in cmds:
        if cmd == "R":
            if reversed:
                reversed = False
            else:
                reversed = True
        else:
            if reversed:
                q.pop()
            else:
                q.popleft()
    if reversed:
        q.reverse()
    # 1 R 0 [] 일 경우
    if list(q) == ['']:
        return []
    else:
        return list(map(int, list(q)))
    


for _ in range(n):
    cmds = list(input().rstrip())
    len = int(input())
    nums = input().rstrip()[1:-1].split(',')
    result = get_result(cmds, len, nums)
    if result == []:
        print('[]')
    elif result == 'error':
        print('error')
    else:
        print('[', end='')
        print(*result, sep=',', end='')
        print(']')