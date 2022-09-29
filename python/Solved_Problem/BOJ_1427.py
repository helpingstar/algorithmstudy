import sys

input = sys.stdin.readline

string = input().rstrip()

print("".join(reversed(sorted(string))))
