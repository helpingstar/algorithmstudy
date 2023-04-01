import sys

input = sys.stdin.readline

cnt = 0
while True:
    try:
        print(input().split())
    except EOFError:
        break
