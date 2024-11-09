from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         strs_map = {}
        
#         for s in strs:
#             string_sorted = ''.join(sorted(s))
#             if string_sorted  not in strs_map: 
#                 strs_map[string_sorted] = [s]
#             else:
#                 strs_map[string_sorted].append(s)
        
        
#         for key in strs_map.items():
#             result.append(key[1])
        
#         return result


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map= {}
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            
            if sorted_string not in anagrams_map: 
                anagrams_map[sorted_string] = [string]
            else:
                anagrams_map[sorted_string].append(string)
       

        return list(anagrams_map.values())
        
        
    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(sol.groupAnagrams([[""]]))
# print(sol.groupAnagrams(["a"]))
