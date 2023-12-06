import sys

input = sys.stdin.readline

def solution():
    target, n_city = map(int, input().split())
    costs = [0]
    clients = [0]
    for _ in range(n_city):
        a, b = map(int, input().split())
        costs.append(a)
        clients.append(b)
    
    board = [0] * 100001

    for r in range(1, n_city+1):
        cost, client = costs[r], clients[r]
        new_board = [0]
        for c in range(1, len(board)):
            if c < cost:
                new_board.append(board[c])
            else:
                new_board.append(max(board[c-cost] + client, board[c], new_board[c-cost] + client))

            if new_board[-1] >= target:
                board = new_board
                # print(new_board)
                break
                
    # print(board)
    print(len(board)-1)


solution()