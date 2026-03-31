class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        cache={}
        def memo(i,j):
            if i == n:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)]=costs[i][j] + min(memo(i+1,(j+1)%3),memo(i+1,(j+2)%3))
            return cache[(i,j)]
        return min(memo(0,0),memo(0,1),memo(0,2))

        