# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         if sorted(t) == sorted(s):
#             return True
        
#         return False
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        
        
        for c in s:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
            
        for c in t:
            if c in char_map:
                char_map[c] -= 1
            
        for value in char_map.values():
            if value != 0:
                return False
        
        return True 
        
        
sol = Solution()
print(sol.isAnagram("anagram", "nagara"))