from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idxI, i in enumerate(nums):
        for idxJ, j in enumerate(nums):
            if i + j == target and idxI != idxJ:
                return [idxI,idxJ]
                


sol = Solution()

print(sol.twoSum([2,7,11,15], 9))