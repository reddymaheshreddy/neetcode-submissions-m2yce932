class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         num={}
         for ele in nums:
            s=f"{ele}"
            if s in num:
                num[s]=num[s]+1
            else:
                num[s]=1
            if num[s] > 1:
                return True
         return False