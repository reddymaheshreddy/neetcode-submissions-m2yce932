
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set(nums)
        my_dict={}
        maxi=0
        for ele in my_set:
            my_dict[ele] = 1
            y=ele + 1
            if y in my_dict:
                my_dict[ele]+=my_dict[ele+1]
            else:
                while y in my_set:
                    my_dict[ele]+=1
                    y=y+1
            maxi=max(maxi,my_dict[ele])
        return maxi
