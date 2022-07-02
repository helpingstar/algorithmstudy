class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        n_unit = numRows*2 - 2
        s_len = len(s)
        if s_len % n_unit == 0:
            first = s_len // n_unit
        else:
            first = s_len // n_unit + 1
        
        if s_len % n_unit >= numRows:
            last = s_len // n_unit + 1
        else:
            last = s_len // n_unit
        
        ans = ''
        
        # first
        for i in range(first):
            ans += s[i*n_unit]
        
        
        for i in range(numRows-2):
            cnt = i+1
            front = True
            diff = [n_unit - cnt*2, cnt*2]
            while cnt < s_len:
                ans += s[cnt]
                if front:
                    cnt += diff[0]
                else:
                    cnt += diff[1]
                if front:
                    front = False
                else:
                    front = True
                
        # last
        for i in range(last):
            ans += s[numRows-1 + i*n_unit]
            
        return ans