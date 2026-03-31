class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        temp=[]
        l = len(nums)
        def backtrack(i):
            if i >= l:
                res.append(temp[:])
                return
            
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        return res
        

        


            
        