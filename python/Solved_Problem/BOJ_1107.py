import sys

input = sys.stdin.readline

channel = int(input())
m = int(input())
if m == 0:
    print(min(len(str(channel)), abs(channel-100)))
else:
    broken = set(input().split())
    result = 1000000
    for i in range(1000001):
        temp = set(str(i))
        if temp & broken:
            continue
        if result > len(str(i)) + abs(i - channel):
            result = len(str(i)) + abs(i - channel)

    print(min(abs(100-channel), result))
