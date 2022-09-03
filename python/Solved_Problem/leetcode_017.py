class Solution:   
    def letterCombinations(self, digits: str) -> List[str]:
        self.n2a = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        self.answer = []
        self.digits = digits
        self.len_input = len(digits)
        
        if digits == "":
            return []
        
        self.dp('', 0)
        return self.answer
    
    def dp(self, string, x):
        if self.len_input == x:
            self.answer.append(string)
            return
        else:
            for i in self.n2a[int(self.digits[x])]:
                self.dp(string + i, x+1)

digits = "23"

a = Solution()
print(a.letterCombinations(digits))