n = int(input())
graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]

def recursive(N, before):
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        after[i][N:N+2*N-1] = before[i]

    k = 0
    for i in range(N, 2 * N):
        after[i][:2*N] = before[k]
        after[i][2 * N:2 * N+len(before[k])] = before[k]
        k += 1

    if 2 * N == n:
        return after

    return recursive(2 * N, after)

if n == 3:
    result = graph
else:
    result = recursive(3, graph)

for i in result:
    print("".join(i))





# ----------------------------------------------------------------------

n = int(input())
graph = [[' '] * 2 * n for _ in range(n)]


def recursive(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        nextN = N // 2
        recursive(x, y, nextN)
        recursive(x + nextN, y - nextN, nextN)
        recursive(x + nextN, y + nextN, nextN)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))
