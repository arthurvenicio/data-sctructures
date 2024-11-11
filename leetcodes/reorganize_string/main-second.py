import heapq

class Solution: 
    def reorganizeString(self, s: str) -> str:
        freq_char_map = {}
        for char in s:
            freq_char_map[char] = freq_char_map.get(char, 0) + 1
            
        max_heap = [(-freq, char) for char, freq in freq_char_map.items()]
        heapq.heapify(max_heap)
    
        prev = None
        res = ""
        
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            freq, char = heapq.heappop(max_heap)
            res += char
            freq += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
                
            if freq < 0:
                prev = (freq, char)
            
        return res
        
      
      
      
sol = Solution()

  
print(sol.reorganizeString("aaabbcc"))