# Merge Sort방법

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        arr = []
        length = len(nums1) + len(nums2)
        
        for i in range(length):
            if p1 >= len(nums1):
                arr += nums2[p2:]
                break
            if p2 >= len(nums2):
                arr += nums1[p1:]
                break
                
            if nums1[p1] < nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
            else:
                arr.append(nums2[p2])
                p2 += 1
        
        if length % 2 == 0:
            return ((arr[length//2] + arr[length//2 - 1]) / 2)
        else:
            return (arr[length // 2])