from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        nums.sort()
        
        return nums[len(nums) - k]
    
    
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))