class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        curr = 0
        for i in range(n-2,-1,-1):
            curr = one + two
            two = one
            one = curr
            curr = 0
        return one
            
