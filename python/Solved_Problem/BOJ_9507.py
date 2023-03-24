import sys

input = sys.stdin.readline

fibo = [0] * 68
fibo[0], fibo[1], fibo[2], fibo[3], fibo[4] = 1, 1, 2, 4, 8
for i in range(5, 68):
    fibo[i] = fibo[i-1] + fibo[i-1] - fibo[i-5]

for _ in range(int(input())):
    print(fibo[int(input())])
