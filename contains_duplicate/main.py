class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for idx, num in enumerate(nums):
            if num in freq_map:
                return True
            else:
                freq_map[num] = idx

        return False

# here we use dictonary (hashmap)   
        
# another solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set  = set(nums)
        
        return True if len(nums_set) < len(nums) else False
    
# here we use set (hashmap)  