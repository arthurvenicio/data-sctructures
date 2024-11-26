
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter_map = {}
        
        for num in nums:
            counter_map[num] = 1 + counter_map.get(num, 0)
            
        max_heap =[]
        for key, val in counter_map.items():
            heapq.heappush(max_heap, (-val, key))
        
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res
    
sol = Solution()

# print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([-1,-1], 1))