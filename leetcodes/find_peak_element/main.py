from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            mid_val = nums[mid]
            mid_left_value = nums[mid - 1] if mid > 0 else float('-inf')
            mid_right_value = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            
            if mid_left_value < mid_val > mid_right_value :
                return mid_val
            elif mid_left_value < mid_val < mid_right_value:
                left = mid + 1
            else:
                right = mid - 1
                
    
sol = Solution()

print(sol.findPeakElement([1,2,3,1]))