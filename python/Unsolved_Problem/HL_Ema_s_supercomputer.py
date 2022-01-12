#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#


def twoPluses(grid):
    # Write your code here
    row = len(grid)
    col = len(grid[0])
    
    # The longest possible branch length (excluding center)
    longest_branch_len = int((min((row, col)) - 1) // 2)
    
    exist_point = []
    
    # Check that's more than 3 spaces.
    for branch_len in range(longest_branch_len, 0, -1):
        for r in range(branch_len, row-branch_len):
            for c in range(branch_len, col-branch_len):
                # check whether it is valid plus
                plus_available=True
                for y in range(r-branch_len, r+branch_len+1):
                    if grid[y][c] == 'B':
                        plus_available=False
                        break
                if plus_available:
                    for x in range(c-branch_len, c+branch_len+1):
                        if grid[r][x] == 'B':
                            plus_available=False
                            break
                # check whether it is already_exist
                valid_position = True
                # exist_point is None
                if not exist_point:
                    pass
                else:
                    exist_r, exist_c, exist_l = exist_point[0][0], exist_point[0][1], exist_point[0][2]
                    
                    if exist_r == r:
                        if (exist_c - exist_l - branch_len) <= c <= (exist_c + exist_l + branch_len):
                            valid_position = False
                    elif exist_c == c:
                        if (exist_r - exist_l - branch_len) <= r <= (exist_r + exist_l + branch_len):
                            valid_position = False
                    elif ((exist_r - exist_l) <= r <= (exist_r + exist_l)) and ((exist_c - exist_l) <= c <= (exist_c + exist_l)):
                        if ((exist_r - branch_len) <= r <= (exist_r + branch_len)) or ((exist_c - branch_len) <= c <= (exist_c + branch_len)):
                            valid_position = False
                        
                if plus_available and valid_position:
                    exist_point.append([r, c, branch_len])
                if len(exist_point) == 2:
                    # print(2)
                    # print((exist_point[0][2] * 4 + 1) * (exist_point[1][2] * 4 + 1))
                    # return exist_point
                    return (exist_point[0][2] * 4 + 1) * (exist_point[1][2] * 4 + 1)
    
    # not exist valid plus
    if not exist_point:
        return 1
    
    # One space check.
    # print(1)
    # print(exist_point[0][2] * 4 + 1)
    # return exist_point
    return exist_point[0][2] * 4 + 1
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(result)
