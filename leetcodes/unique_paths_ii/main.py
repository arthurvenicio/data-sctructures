from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Start position

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # No paths through an obstacle
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]  # Paths from above
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]  # Paths from the left

        return dp[-1][-1]
