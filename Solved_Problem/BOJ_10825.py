import sys

n = int(sys.stdin.readline())

st_list = []

for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    st_list.append((name, int(kor), int(eng), int(math)))

st_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for l in st_list:
    print(l[0])