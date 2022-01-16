import sys
input = sys.stdin.readline

n = int(input())

rgb_cost = [[0, 0, 0]]
for _ in range(n):
    rgb_cost.append(list(map(int, input().split())))

home_cost = [[0, 0, 0] for _ in range(n+1)]

for i in range(3):
    home_cost[1][i] = rgb_cost[1][i]

# 여기서 각 테이블을 구성하는 방법도 있지만
# r, g, b로 구성하여서 그냥 누적합을 구하여도 된다. ex) now_r += min(old_g, old_b)
# 이 경우에 입력 즉시 처리하면 되므로 메모리가 줄고 코드가 간결해지는 효과가 있다.

for i in range(2, n+1):
    home_cost[i][0] = min((home_cost[i-1][1], home_cost[i-1][2])) + rgb_cost[i][0]
    home_cost[i][1] = min((home_cost[i-1][0], home_cost[i-1][2])) + rgb_cost[i][1]
    home_cost[i][2] = min((home_cost[i-1][0], home_cost[i-1][1])) + rgb_cost[i][2]

print(min(home_cost[n]))