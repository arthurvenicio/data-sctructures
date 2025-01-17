from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left 
    
    
sol = Solution()
arr = [3,2,2,3]
print(sol.removeElement(arr, 3))
print(arr)