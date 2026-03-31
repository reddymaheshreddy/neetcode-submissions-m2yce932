from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high)//2
            total =0 
            for pile in piles:
                total += ceil(pile/mid)
            if total > h:
                low =mid+1
            else:
                high = mid - 1
        return low
            
        