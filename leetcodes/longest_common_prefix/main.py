from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
                
        i = 0
        
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]            
            i += 1
            
        return s[:i]
    
    # time complexity: O(n * m)
    # space : O(1)
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))