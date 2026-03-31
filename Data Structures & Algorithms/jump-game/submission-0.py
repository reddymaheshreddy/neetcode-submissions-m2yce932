class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi_index=nums[0]
        n=len(nums)
        for j in range(1,n):
            if maxi_index >= n:
                return True
            if j > maxi_index:
                return False
            maxi_index = max(maxi_index,j+nums[j])
        return True 
            

        