class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-3,-2,-2,0,1,1,2,3]
        
        """
        nums.sort()
        res=[]
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            k = len(nums)-1
            j = i+1
            while j < k :
                while j > i+1 and j < k and nums[j] == nums[j-1]:
                    j+=1
                while k < l -1 and j < k and nums[k] == nums[k+1]:
                    k-=1
                if j >= k :
                    break
                    
                curr = nums[j]+nums[k]
                if curr == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif curr < target:
                    j+=1
                else:
                    k-=1
                
        return res
                    
                    


                

        