class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            m = (l + r) // 2
            m_sq = m * m

            if num == m_sq:
                return True

            elif m_sq < num:
                l = m + 1
            else:
                r = m - 1

        return False