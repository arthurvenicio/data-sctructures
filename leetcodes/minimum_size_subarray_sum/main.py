class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        l = 0
        summ = 0
        n = len(nums)

        for r in range(n):
            summ += nums[r]

            while summ >= target:
                min_l = min(min_l, r-l+1)
                summ -= nums[l]
                l +=1

        return min_l if min_l < float('inf') else 0
    
# Time complexity: O(n)
# Space complexity: O(1)