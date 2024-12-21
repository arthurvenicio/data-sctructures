from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        temp = []
        
        def backtrack(start):
            if start == n:
                res.append(temp[:])
                return
        
            backtrack(start + 1)
            temp.append(nums[start])
            backtrack(start + 1)
            temp.pop()
            
        backtrack(0)
        return res


# Time complexity: O(2^n)
# Space complexity: O(n)            