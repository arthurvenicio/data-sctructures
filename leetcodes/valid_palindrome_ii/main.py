# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if len(s) == 1 :
#             return True
        
#         # str_clean = ''.join(e for e in s if e.isalnum()).lower()
        
#         left, right = 0, len(s) - 1
        
#         while left < right:
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
#         return True
    
#     def validPalindrome(self, s: str) -> bool:
#         for i in range(len(s)):
#             str_clean = ''.join(e for idx, e in enumerate(s) if idx != i and e.isalnum())
            
#             if(self.isPalindrome(str_clean)):
#                 return True
        
#         return False
            
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[:left]+ s[left + 1:]) or self.isPalindrome(s[:right]+ s[right + 1:])
            
            left += 1
            right -= 1
            
        return True
            
sol = Solution()

print(sol.validPalindrome("aba"))
print(sol.validPalindrome(" "))