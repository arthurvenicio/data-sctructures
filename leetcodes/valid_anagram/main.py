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
        
        main_string = s if len(s) > len(t) else t
        second_string = t if len(s) < len(t) else s
        
        for c in main_string:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
            
        for c in second_string:
            if c in char_map:
                char_map[c] -= 1
            
        for value in char_map.values():
            if value != 0:
                return False
        
        return True 
        
        
sol = Solution()
print(sol.isAnagram("a", "b"))