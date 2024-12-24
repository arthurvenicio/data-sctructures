class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        counter = 0

        for s in stones:
            if s in j_set:
                counter += 1
        
        return counter