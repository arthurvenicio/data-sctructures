from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Initialize robot's starting position at (0, 0)
        x, y = 0, 0
        
        # Define directions: North, East, South, West as (dx, dy) pairs
        direct = [[0,1], [1,0], [0, -1], [-1, 0]]
        
        d = 0  # Current direction index (starts at North)
        res = 0  # Maximum squared Euclidean distance
        
        # Convert the obstacle list into a set of tuples for fast lookup
        obstacles = {tuple(o) for o in obstacles}
        
        for c in commands:  # Process each command
            if c == -1:  # Turn right (increment direction index clockwise)
                d = (d + 1) % 4
            elif c == -2:  # Turn left (decrement direction index counterclockwise)
                d = (d - 1) % 4
            else:  # Move forward
                dx, dy = direct[d]  # Get the current direction
                
                for _ in range(c):  # Move step by step
                    if (x + dx, y + dy) in obstacles:  # Stop if hitting an obstacle
                        break
                    x, y = x + dx, y + dy  # Update the position
                    
            # Update the maximum squared Euclidean distance
            res = max(res, x**2 + y**2)
        
        return res  # Return the maximum distance

# Time Complexy: O(c + p) where c is the sum of commands and p is the total of commands
# Space Complexy: O(o) where o is the num of obstacles