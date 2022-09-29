from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            dic[''.join(sorted(word))].append(word)

        ans = []
        for arr in dic.keys():
            ans.append(list(dic[arr]))
        return ans

strs = ["eat","tea","tan","ate","nat","bat"]

a = Solution()
print(a.groupAnagrams(strs))
