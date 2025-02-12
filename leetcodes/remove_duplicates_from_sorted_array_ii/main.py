from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        
        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        
        return left
    
    
# Time complexity: O(n)
# Space complexity: O(1)
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))