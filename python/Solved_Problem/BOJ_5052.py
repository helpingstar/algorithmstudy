import sys

input = sys.stdin.readline


def solution():
    for _ in range(int(input())):
        print(emergency())


def emergency():
    numbers = []
    C = int(input())
    for _ in range(C):
        number = input().rstrip()
        numbers.append(number)
    numbers.sort()
    # print(numbers)
    for i in range(C-1):
        if len(numbers[i]) >= len(numbers[i+1]):
            continue
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return "NO"
    return "YES"


solution()
