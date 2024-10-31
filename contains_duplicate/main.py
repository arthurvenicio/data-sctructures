class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for idx, num in enumerate(nums):
            if num in freq_map:
                return True
            else:
                freq_map[num] = idx

        return False
        