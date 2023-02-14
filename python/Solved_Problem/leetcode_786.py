from typing import *

from itertools import combinations

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fracs = []
        combis = list(combinations(arr, 2))
        combis.sort(key=lambda x: x[0] / x[1])
        return list(combis[k-1])
