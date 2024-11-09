from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr_sorted = sorted(nums1 + nums2)
        mid  = len(arr_sorted) // 2
        
        return arr_sorted[mid]
        
sol = Solution()

print(sol.findMedianSortedArrays([1,3], [2]))