class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [height,ind]
        maximum = 0
        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h,ind = stack.pop()
                maximum = max(maximum,h*(i-ind))
                start = ind
            stack.append([height,start])
        l = len(heights)
        for height,i in stack:
            maximum = max(maximum,height * (l-i))
        return maximum

        