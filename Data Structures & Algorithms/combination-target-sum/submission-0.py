class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        n=len(nums)
        def backtrack(total,i):
            if total == target:
                res.append(temp[:])
                return
            if i >= n :
                return 
            for j in range(i,n):
                if total + nums[j] > target:
                    return 
                temp.append(nums[j])
                backtrack(total+nums[j],j)
                temp.pop()
        backtrack(0,0)
        return res

        