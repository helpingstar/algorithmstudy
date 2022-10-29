from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        finish = 0
        cur = 0
        ans = []
        while cur < len(intervals):
            start = intervals[cur][0]
            finish = intervals[cur][1]
            while cur < len(intervals) and intervals[cur][0] <= finish:
                finish = max(finish, intervals[cur][1])
                cur += 1
            ans.append([start, finish])
        return ans



intervals = [[1,4]]
a = Solution()
print(a.merge(intervals))
