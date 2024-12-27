from cmath import inf
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_ar = float(-inf)

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            max_ar = max(area, max_ar)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_ar

# Time complexity: O(n)
# Space complexity: O(1)
