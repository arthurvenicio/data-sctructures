class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        n = len(s)
        counts = [0] * 26

        for right in range(n):
            counts[ord(s[right]) - 65] += 1
            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
            
            res = max(res, (right - left + 1))
            
        return res
    
# Methoud: Sliding Windown
# Time complexity: O(n)
# Space complexity: O(1)