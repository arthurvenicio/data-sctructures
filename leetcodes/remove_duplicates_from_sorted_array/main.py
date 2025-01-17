from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1

            
        
sol = Solution()
arr = [0,0,1,1,1,2,2,3,3,4]
print(arr)