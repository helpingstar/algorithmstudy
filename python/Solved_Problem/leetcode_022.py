from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def dp(now, opened, closed):
            if len(now) == 2*n:
                self.ans.append(now)
                return
            if opened == closed:
                dp(now + "(", opened+1, closed)
            else:
                if opened == n:
                    dp(now + ")", opened, closed+1)
                else:
                    dp(now + "(", opened+1, closed)
                    dp(now + ")", opened, closed+1)
        dp("", 0, 0)
        return self.ans
