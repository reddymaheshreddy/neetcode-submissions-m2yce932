from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque([])
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
        while queue:
            i,j=queue.popleft()
            for r,c in [[0,1],[1,0],[0,-1],[-1,0]]:
                row = i+r
                col = j+c
                if 0<=row<rows and 0<=col<cols and grid[row][col] == 2147483647:
                    
                    grid[row][col] = 1+grid[i][j]
                    
                    queue.append([row,col])
        
        
        
        