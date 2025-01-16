from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sub_total = 0
        buckets = defaultdict(list)
        
        # we create the buckets, separete the words by the first char
        for word in words:
            buckets[word[0]].append(word)
        
        
        # iterate over char in the string
        for c in s:
            bucket = buckets[c]
            buckets[c] = []
            
            # iterate over words of the bucket
            for word in bucket:
                if len(word) == 1:
                    sub_total += 1
                else:
                    buckets[word[1]].append(word[1:])
        
        return sub_total

# Method: Using dictionary to create buckets
# n = len(s)
# m = len(words)
# Time complexity: O(n * m)
# Space complexity: O(m)


sol = Solution()
print(sol.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))