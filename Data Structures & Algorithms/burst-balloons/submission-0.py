class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        [4,2,3,7]
        """
        l = len(nums)
        cache ={}

        def dp(i,j):
            if i > j:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            maxi = 0

            for k in range(i, j+1):
                left = 1 if i == 0 else nums[i-1]
                right = 1 if j == l-1 else nums[j+1]

                coins = left * nums[k] * right

                maxi = max(maxi, coins + dp(i,k-1) + dp(k+1,j))

            cache[(i,j)]= maxi
            return cache[(i,j)]

        return dp(0,l-1)

                