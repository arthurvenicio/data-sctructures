class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        reversed = 0
        temp = x
        
        while temp != 0:
            digit = temp % 10 # the rest of dividing a number by 10 the is the last digit
            reversed = reversed * 10 + digit 
            temp = temp // 10
        
        return x == reversed
    
sol = Solution()

print(sol.isPalindrome(121))
print(sol.isPalindrome(11))
print(sol.isPalindrome(10))