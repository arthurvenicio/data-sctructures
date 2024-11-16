class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
       
        for i in range(len(s)):
            left = right = i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > (end - start):
                start  = left + 1
                end = right - 1

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > (end - start):
                start  = left + 1
                end = right - 1

            s [start:end + 1]