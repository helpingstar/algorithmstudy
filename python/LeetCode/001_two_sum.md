# 내 풀이
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
전형적인 Brute Force

# 다른 답
## `HashTable`
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
```

위의 답은 Hash에 추가하면서 있는지 없는지를 검사하고 아래의 답은 한번에 다 추가하고 찾는다. 두번째가 더 빠르게 나왔고 이유를 추정해보자면 a + b == target일 때 첫 번째 답은 뒤에 있는 b를 찾을 때 답이 나오는데 두번째 답은 앞에 있는 a를 찾아도 답을 찾을 수 있기 때문인 듯 하다.

## 기타
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = 0, 0
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                a = i
                b = i + 1 + nums[i+1:].index(target-nums[i])
                break
        return [a, b]
```
Brute Force보다 빠르다. a를 순차탐색하고 나머지 a+1 ~ end 범위에서 만족하는 숫자가 있는지 찾는다. index의 search알고리즘이 단순 for문보다 좋아서 빠른 것 같다.