class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            visited.add((i,j))
            for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                if 0<=i+r<rows and 0<=j+c<cols and (i+r,j+c) not in visited and grid[i+r][j+c] == "1":
                    dfs(i+r,j+c)
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] =="1":
                    total+=1
                    dfs(i,j)
        return total
            