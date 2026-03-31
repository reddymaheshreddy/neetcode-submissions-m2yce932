class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 1
        curr_jump = nums[0]
        max_jump = nums[0]
        if len(nums) == 1:
            return 0

        n = len(nums)
        for j in range(1,n):
            if curr_jump < j:
                curr_jump = max_jump
                steps+=1
            max_jump = max(max_jump,j+nums[j])
        return steps
        