"""
N과 K의 최대값이 100,000이므로 브루트포스의 경우
10,000,000,000 번의 계산이므로 1초보다 무조건 넘는다.

lights를 list -> tuple : 96 -> 68
"""
import sys

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    lights = tuple(map(int, input().split()))
    checker = [0] * N
    flag = 0
    cnt = 0
    for i in range(K):
        if lights[i] ^ flag:
            cnt += 1
            checker[i] = 1
            flag ^= 1

    for i in range(K, N - K + 1):
        if checker[i - K] == 1:
            flag ^= 1
        if lights[i] ^ flag:
            cnt += 1
            checker[i] = 1
            flag ^= 1

    for i in range(N - K + 1, N):
        if checker[i - K] == 1:
            flag ^= 1
        if lights[i] ^ flag:
            return 'Insomnia'
    return cnt

if __name__ == "__main__":
    print(solution())
