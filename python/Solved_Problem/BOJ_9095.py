import sys

n = int(sys.stdin.readline().rstrip())

case_list = [0] * 11

case_list[1] = 1
case_list[2] = 2
case_list[3] = 4

for i in range(4, 11):
    case_list[i] = case_list[i-1] + case_list[i-2] + case_list[i-3]
    
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    print(case_list[m])