#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    tree = [0] * (1 << (math.ceil(math.log2(200)) + 1))

    def update(start, end, index, node, diff):
        if index < start or end < index:
            return
        tree[node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        update(start, mid, index, node*2, diff)
        update(mid+1, end, index, node*2 + 1, diff)

    def find(start, end, node, k):
        if start == end:
            return start
        mid = (start + end) // 2
        if tree[node*2] >= k:
            return find(start, mid, node*2, k)
        else:
            return find(mid+1, end, node*2+1, k - tree[node*2])

    for i in range(d):
        update(0, 200, expenditure[i], 1, 1)
    result = 0
    for i in range(d, n):
        if d % 2 == 0:
            a = find(0, 200, 1, d//2)
            b = find(0, 200, 1, d//2 + 1)
            median = (a + b) / 2
        else:
            median = find(0, 200, 1, d//2 + 1)
        if expenditure[i] >= 2 * median:
            result += 1
        update(0, 200, expenditure[i-d], 1, -1)
        update(0, 200, expenditure[i], 1, 1)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
