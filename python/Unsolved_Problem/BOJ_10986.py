"""import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0

visited = defaultdict(int)

def is_mod_zero(num):
    return True if num % m == 0 else False

def get_mod(start, end, sum):
    global ans
    if is_mod_zero(sum):
        if visited[(start, end)] < 1:
            ans += 1
            visited[(start, end)] += 1
    if start == end:
        return
    
    get_mod(start+1, end, sum-arr[start])
    get_mod(start, end-1, sum-arr[end])

get_mod(0, n-1, sum(arr))
print(ans)
"""

import sys
input = sys.stdin.readline
total, tar = map(int, input().split())

tem = list(map(int, input().split()))

prepix = [0 for i in range(tar)]
presum = 0
prepix[0] = 1


for i in range(total):
    presum+=tem[i]
    # prepix.append(presum%tar)

    prepix[presum%tar] += 1

# print(prepix)
'''
나머지가 같은 두 부분합을 고르면 두 구간은 결국 tar의 배수가 된다.
나머지가 0인 경우는 부분합 자체가 tar의 배수인 경우이므로 두 구간이 아니라 본인 구간도 될 수 있기 때문에
index가 0인 (부분합 0) 것을 포함
'''
ans=0
for i in prepix:
    ans += i*(i-1)//2

print(ans)