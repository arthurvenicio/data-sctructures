class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        
        str_clean = ''.join(e for e in s if e.isalnum()).lower()
        
        left, right = 0, len(str_clean) - 1
        
        while left < right:
            if str_clean[left] == str_clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        
sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))