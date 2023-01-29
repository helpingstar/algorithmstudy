from collections import defaultdict

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1dict = defaultdict(int)
        ver2dict = defaultdict(int)
        for i, num in enumerate(version1.split('.')):
            ver1dict[i] = int(num)
        for i, num in enumerate(version2.split('.')):
            ver2dict[i] = int(num)

        length = max(len(ver1dict), len(ver2dict))

        for i in range(length):
            if ver1dict[i] < ver2dict[i]:
                return -1
            elif ver1dict[i] > ver2dict[i]:
                return 1
        return 0
