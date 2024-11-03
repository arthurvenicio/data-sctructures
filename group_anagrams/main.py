from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        strs_map = {}
        
        for s in strs:
            string_sorted = ''.join(sorted(s))
            if string_sorted  not in strs_map: 
                strs_map[string_sorted] = [s]
            else:
                strs_map[string_sorted].append(s)
        
        
        for key in strs_map.items():
            result.append(key[1])
        
        return result
        
    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(sol.groupAnagrams([[""]]))
# print(sol.groupAnagrams(["a"]))
