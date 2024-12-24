class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_freq = {}

        for x in text:
            if x in hash_freq:
                hash_freq[x] += 1
            else:
                hash_freq[x] = 1

        return min(hash_freq.get("b", 0), hash_freq.get("a", 0), hash_freq.get("l", 0)//2, hash_freq.get("o", 0)//2, hash_freq.get("n", 0))
        