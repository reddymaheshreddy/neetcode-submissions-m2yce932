class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=height[0]
        maximum_left=[0]
        for h in height[1:]:
            maximum_left.append(maxLeft)
            maxLeft=max(maxLeft,h)
        maxRight=height[-1]
        maximum_right=[0]
        for i in range(len(height)-2,-1,-1):
            maximum_right.append(maxRight)
            maxRight=max(maxRight,height[i])
        maximum_right.reverse()
        res=0
        for h,mL,mR in zip(height,maximum_left,maximum_right):
            if h < mL and h < mR:
                res+= min(mL,mR)-h
        return res
