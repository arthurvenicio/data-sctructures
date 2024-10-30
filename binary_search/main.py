class Solution:
    def __init__(self) -> None:
        self = self
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if(nums[mid] < target):
                left = mid + 1
            else:
                right = mid
        
        return -1
    
    
sol = Solution()

print(sol.binarySearch([1,2,3,4,5], 2))
        