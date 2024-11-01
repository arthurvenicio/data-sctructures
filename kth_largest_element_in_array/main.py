import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for i in nums[k:]:
            if i > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, i)
        
        return min_heap[0]
        

    
    
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

# nums =  3,2,1,5,6,4  k = 2
# result = 5


# nums = [3,2,3,1,2,4,5,5,6] k = 4
# 3,2,3,1 -> 1,2,3,3 after heapify
# for ->  2,4,5,5,6
# 2,3,3,2
# for ->  4,5,5,6
# 3,3,2,4
# for ->  5,5,6
# 3,2,4,5
# for ->  5,6
# 2,4,5,5
# for ->  6
# 4,5,5,6


# result = 4

# for this case, i'm using max_heap O(n + k logn)