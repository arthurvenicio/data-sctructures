from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs)):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))