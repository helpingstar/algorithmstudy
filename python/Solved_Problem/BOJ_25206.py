import sys

input = sys.stdin.readline

cnt = 0
result = 0

g_map = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

while True:
    try:
        _, b, grade = input().split()
        if grade != 'P':
            result += float(b) * g_map[grade]
            cnt += float(b)
    except:
        break

print(result/cnt)
