class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions=set()
        visited = set()
        row=len(grid)
        col=len(grid[0])
        
        def dfs(r,c,temp):
            visited.add((r,c))
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                x = dx+r
                y = dy+c
                if 0<=x<row and 0<=y<col and (x,y) not in visited and grid[x][y]==1:
                    temp.append((dx,dy))
                    dfs(x,y,temp)
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == 1:
                    temp = []
                    dfs(i,j,temp)
                    
                    tup = tuple(temp[:])
                    
                    directions.add(tup)
        return len(directions)

        