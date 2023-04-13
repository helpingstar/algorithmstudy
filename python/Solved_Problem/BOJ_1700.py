import sys

input = sys.stdin.readline

N, K = map(int, input().split())

tools = list(map(int, input().split()))

plugs = []
ans = 0
for i, tool in enumerate(tools):
    # print(plugs)
    if tool in plugs:
        continue
    if len(plugs) < N:
        plugs.append(tool)
        continue


    temp = 0
    behind = -1
    for j, plug in enumerate(plugs):
        if plug not in tools[i:]:
            temp = j
            break
        else:
            new_index = tools[i:].index(plug)
            if new_index > behind:
                behind = new_index
                temp = j
    plugs[temp] = tool
    ans += 1

# print(plugs)
print(ans)
