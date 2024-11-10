from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        # we must iterate over each element, change the signal to negative. 
        # If the number alreay is negative, we already iterate over in this number, so we have a duplicate. 
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] <0:
                result.append(index + 1)
            nums[index] = -nums[index]

        return result
        
        
# Time Complexity : O(n)
# Space Complexity: O(1)