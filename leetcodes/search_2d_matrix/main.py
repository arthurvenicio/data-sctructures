class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        t = m * n
        l, r = 0, t - 1 

        while l <= r:
            m  = (l + r) // 2
            i = m // n
            j = m % n

            val = matrix[i][j]

            if val == target:
                return True
            
            if target < val:
                r = m - 1
            else:
                l = m + 1
        

        return False
        