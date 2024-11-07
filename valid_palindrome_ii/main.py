class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        
        # str_clean = ''.join(e for e in s if e.isalnum()).lower()
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            str_clean = ''.join(e for idx, e in enumerate(s) if idx != i and e.isalnum())
            
            if(self.isPalindrome(str_clean)):
                return True
        
        return False
            
            
            
sol = Solution()

print(sol.validPalindrome("abc"))