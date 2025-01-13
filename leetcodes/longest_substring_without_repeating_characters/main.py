class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0 
        res = 0
        n = len(s)

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            char_set.add(s[right])

        return res
    
# Time complexity: O(n)
# Space complexity: O(1)
# Method: Slide widown