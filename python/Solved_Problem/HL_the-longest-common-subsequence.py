#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def longestCommonSubsequence(a, b):
    # Write your code here
    n, m = len(a), len(b)
    board = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if b[i] == a[j]:
                board[i+1][j+1] = board[i][j] + 1
            else:
                board[i+1][j+1] = max(board[i+1][j], board[i][j+1])

    print(board[-1][-1])
    result = []
    # r, c = m, n

    while m >= 0 and n >= 0:
        print(m, n)
        if b[m-1] == a[n-1]:
            result.append(b[m-1])
            m -= 1
            n -= 1
        else:
            if board[m-1][n] > board[m][n-1]:
                m -= 1
            else:
                n -= 1

    return reversed(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
