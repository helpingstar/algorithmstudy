import sys

input = sys.stdin.readline

n = int(input())

wheel_list = []
wheel_length = []

for _ in range(n):
    wheel = input().rstrip()
    wheel_list.append(wheel)
    wheel_length.append(len(wheel))

target = input().rstrip()

print(wheel_list)
print(wheel_length)
