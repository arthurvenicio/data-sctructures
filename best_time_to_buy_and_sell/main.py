from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        visit_map = {}
        
        for idx, price in enumerate(prices):
            visit_map[idx]= price
            
        best_day_buy = 0
        best_day_sell = 1
        
        for day, price in visit_map.items():
            if price < visit_map[best_day_buy] and price != 0 and day != len(prices) - 1:
                best_day_buy = day

        for day, price in visit_map.items():
            if price > visit_map[best_day_sell] and day > best_day_buy:
                best_day_sell = day
                
        if best_day_sell < best_day_buy:
            return 0

        return max(visit_map[best_day_sell] - visit_map[best_day_buy], 0)
    
sol = Solution()
# print(sol.maxProfit([7,1,5,3,6,4]))
# print(sol.maxProfit([7,6,4,3,1]))
# print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([2,1,2,0,1]))