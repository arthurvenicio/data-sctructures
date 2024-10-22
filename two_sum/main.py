class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:

      dic = {}

      for idx, ch in enumerate(nums):
          diff = target - nums[idx]
          if diff in dic:
              return [dic[diff], idx]
          dic[ch] = idx