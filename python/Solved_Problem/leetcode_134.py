from typing import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        possible = 0
        start = 0
        surplus = 0

        for i in range(length):
            diff = gas[i] - cost[i]
            possible += diff
            surplus += diff
            if surplus < 0:
                surplus = 0
                start = i + 1
        if possible < 0:
            return -1
        else:
            return start
