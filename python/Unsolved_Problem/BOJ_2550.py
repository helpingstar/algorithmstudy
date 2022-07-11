import sys
import bisect
input = sys.stdin.readline


n = int(input())
INF = 10001
left = list(map(int, input().split()))
right = list(map(int, input().split()))

mem = [INF] * n
ans_cnt = 0
ans = []

for r in right:
    l_idx = left.index(r)
    mem_idx = bisect.bisect_left(mem, l_idx)
    if l_idx < mem[mem_idx]:
        if mem[mem_idx] == INF:
            ans = mem[:mem_idx] + [l_idx]
        mem[mem_idx] = l_idx

print(len(ans))
real_ans = []
for i in ans:
    real_ans.append(left[i])
print(*sorted(real_ans))