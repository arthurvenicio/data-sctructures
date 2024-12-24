from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        ans = 0
        max_count = -1

        for key, val in dic.items():
            if val > max_count:
                max_count = val
                ans = key

        return ans
        