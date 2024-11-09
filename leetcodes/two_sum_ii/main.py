from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq_map = {}

        for idx, num in enumerate(numbers):
            diff = target - numbers[idx]
            
            if diff in freq_map:
                return [freq_map[diff] + 1, idx + 1]
            
            freq_map[num] = idx
        
    
# Very simple, like the version 1 but here the return id in descending order


sol = Solution()

print(sol.twoSum([2,7,11,15], 9))