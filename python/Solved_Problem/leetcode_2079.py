from typing import *

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        refill = capacity
        for i, water in enumerate(plants):
            if water <= capacity:
                capacity -= water
                ans += 1
            else:
                capacity = refill - water
                ans += (i + i + 1)
        return ans
