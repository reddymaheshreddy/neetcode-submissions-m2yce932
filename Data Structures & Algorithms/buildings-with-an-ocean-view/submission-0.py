class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        res=[len(heights)-1]
        cutoff=heights[-1]  
        for i in range(len(heights)-2,-1,-1):
            if heights[i] > cutoff:
                res.append(i)
                cutoff=heights[i]
        res=res[::-1]
        return res
            

