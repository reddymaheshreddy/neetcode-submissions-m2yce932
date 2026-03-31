class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 1
        curr_jump = nums[0]
        max_jump = nums[0]
        if nums[0] == 0:
            return 0
        if nums[0] == 1 and len(nums) == 1:
            return 0

        n = len(nums)
        for j in range(1,n):
            if max_jump<j:
                return 0
            if curr_jump < j:
                curr_jump = max_jump
                steps+=1
            max_jump = max(max_jump,j+nums[j])
        return steps
        