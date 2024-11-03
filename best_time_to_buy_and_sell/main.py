from typing import List


# BRUTE FORCE - NOT THE BEST

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices or len(prices) == 1:
#             return 0
        
#         visit_map = {}
        
#         for idx, price in enumerate(prices):
#             visit_map[idx]= price
            
#         best_day_buy = 0
#         best_day_sell = 1
        
#         for day, price in visit_map.items():
#             if price < visit_map[best_day_buy] and price != 0 and day != len(prices) - 1:
#                 best_day_buy = day

#         for day, price in visit_map.items():
#             if price > visit_map[best_day_sell] and day > best_day_buy:
#                 best_day_sell = day
                
#         if best_day_sell < best_day_buy:
#             return 0

#         return max(visit_map[best_day_sell] - visit_map[best_day_buy], 0)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
     
        buy_price = prices[0] # starting with the first price
        max_profit = 0
        
        for price in prices[1:]: # slince the list, after the first position
            if buy_price > price:
                buy_price = price
                
                
            curr_profit = price - buy_price
            if max_profit < curr_profit:
                max_profit = curr_profit
            
        return max_profit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))