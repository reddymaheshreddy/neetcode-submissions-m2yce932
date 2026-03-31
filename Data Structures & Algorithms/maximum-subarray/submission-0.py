class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_val = nums[0]
        curr = 0
        i= 0
        n = len(nums)
        for j in range(n):
            curr += nums[j]
            maximum_val = max(maximum_val,curr)
            while curr < 0 and i<=j:
                curr-=nums[i]
                i+=1
                if i<=j:
                    maximum_val=max(maximum_val,curr)
        while i<n-1:
            curr-=nums[i]
            i+=1
            maximum_val = max(maximum_val,curr)
        return maximum_val


        