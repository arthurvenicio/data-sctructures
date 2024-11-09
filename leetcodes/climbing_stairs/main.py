class Solution:
    def climbStairs(self, n: int) -> int:
        # Special case: If there is only 1 step, there is only one way to reach it.
        if n == 1:
            return 1
        # Special case: If there are 2 steps, there are two ways to reach them: (1 + 1) or (2).
        if n == 2:
            return 2

        # Initialize two variables to store the results of the previous two step counts. 'prev' is the number of ways for the second last step, and 'curr' is the number of ways for the last step.
        prev = 1
        curr = 2

        # Start a loop from 2 up to n-1, since we have already handled the first two cases (n = 1 and n = 2).
        for i in range(2, n):
            # Update 'prev' and 'curr'. The new value of 'curr' is the sum of the  previous values of 'prev' and 'curr' because to reach the next step, we can come from one step behind (prev) or two steps behind (curr).
            prev, curr = curr, prev + curr

        # Return 'curr', which contains the number of ways to climb a staircase with n steps.
        return curr
