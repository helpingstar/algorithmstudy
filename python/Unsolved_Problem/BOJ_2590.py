import sys
import math
input = sys.stdin.readline

papers = [0] + [int(input()) for _ in range(6)]
my_papers = [0] * 7

def debug(x):
    print(f'after {x}')
    print(f'papers    : {papers} | my_papers : {my_papers} | answer : {answer}')

answer = 0

answer += papers[6]
papers[6] = 0

# debug(6)

# 5
answer += papers[5]
my_papers[1] += (11 * papers[5])
papers[5] = 0

# debug(5)

# 4
answer += papers[4]
my_papers[2] += (5 * papers[4])
papers[4] = 0

# debug(4)

# 3
answer += papers[3] // 4
papers[3] %= 4
if papers[3] > 0:
    answer += 1
    my_papers[3] += (4 - papers[3])
    papers[3] = 0

# debug(3)

# 2
temp = min(papers[2], my_papers[3])
my_papers[3] -= temp
my_papers[1] += temp * 5
papers[2] -= temp

temp = min(papers[2], my_papers[2])
my_papers[2] -= temp
papers[2] -= temp

answer += papers[2] // 9
papers[2] %= 9
if papers[2] > 0:
    answer += 1
    my_papers[2] += (9 - papers[2])
    papers[2] = 0

# debug(2)

# 1
temp = min(papers[1], my_papers[3] * 9)
papers[1] -= temp

temp = min(papers[1], my_papers[2] * 4)
papers[1] -= temp

temp = min(papers[1], my_papers[f1])
papers[1] -= temp

answer += math.ceil(papers[1] / 36)

print(answer)
