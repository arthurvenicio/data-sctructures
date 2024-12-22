from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,cols = len(matrix), len(matrix[0])
        i, j = 0,0
        
        UP,RIGHT,DOWN,LEFT = 0,1,2,3
        direction  = RIGHT
        
        UP_WALL = 0
        RIGHT_WALL = cols
        DOWN_WALL = row
        LEFT_WALL = -1
        
        res = []
        
        while len(res) != row * cols:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP
            else: 
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -=1
                i, j = i+1, j + 1
                UP_WALL += 1
                direction = RIGHT    
        
        return res
    
# Time complexity: O(m * n)
# Space complexity: O(1)