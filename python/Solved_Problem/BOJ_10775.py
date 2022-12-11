import sys

input = sys.stdin.readline

def solution():
    n_gate = int(input())
    n_plane = int(input())
    gate_check = [i for i in range(n_gate+1)]

    plane_list = []
    for _ in range(n_plane):
        plane_list.append(int(input()))
    ans = 0
    for plane in plane_list:
        while True:
            # print(f'[debug]  plane: {plane}')
            if gate_check[plane] == plane:
                ans += 1
                gate_check[plane] -= 1
                break
            else:
                if gate_check[plane] == 0:
                    return ans
                else:
                    next_plane = gate_check[plane]
                    gate_check[plane] -= 1
                    plane = next_plane
        # print(f'[debug]  gate_check: {gate_check}')
    return ans
print(solution())
