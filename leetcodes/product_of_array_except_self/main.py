from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_multi = 1
        r_multi = 1
        
        l_arr = [0] * n
        r_arr = [0] * n
        
        for i in range(n):
            j = -i - 1
            
            l_arr[i] = l_multi
            r_arr[j] = r_multi
            
            l_multi *= nums[i]
            r_multi *= nums[j]
            
        return [x*y for x, y in zip(l_arr, r_arr)]
    
# Time complexy : O(n)
# Space complexy: O(n)