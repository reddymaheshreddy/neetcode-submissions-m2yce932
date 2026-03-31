class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
    # Base case: If n is negative, return 0 (invalid way)
        if n < 0:
            return 0
    
    # Recursive case: sum of the ways from n-1 and n-2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
