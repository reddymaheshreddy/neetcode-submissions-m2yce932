import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)]
        visit = set()
        time = grid[0][0]
        n = len(grid)
        while heap :
            elevation,x,y = heapq.heappop(heap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            time = max(time,elevation)
            if (x,y) == (n-1,n-1):
                return time
            for nr,nc in [[0,1],[1,0],[0,-1],[-1,0]]:
                r = nr+x
                c = nc +y
                if 0<=r<n and 0<=c<n and (r,c) not in visit:
                    heapq.heappush(heap,(grid[r][c],r,c))


        