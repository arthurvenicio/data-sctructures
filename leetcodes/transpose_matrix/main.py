from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix) # get number of rows 
        c = len(matrix[0]) # get number of columns
        mx = [[0] * r for _ in range(c)] # create a new matrix with the same size as the original matrix
        
        for r in range(r): # iterating over each row
            for c in range(c): # iterating over each collumn
                mx[c][r] = matrix[r][c] 

        return mx
        
# Time complexity: O(m * n)
# [[1,2,3]
#  [4,5,6]
#  [7,8,9]
# ]
sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))