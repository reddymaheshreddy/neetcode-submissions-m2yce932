class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            visited.add((i, j))
            area = 1  # count current cell

            for r, c in [(0,1), (1,0), (-1,0), (0,-1)]:
                ni, nj = i + r, j + c
                if (
                    0 <= ni < rows and
                    0 <= nj < cols and
                    (ni, nj) not in visited and
                    grid[ni][nj] == 1
                    ):
                    area += dfs(ni, nj)

            return area

        maxi = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    maxi = max(maxi, dfs(i, j))

        return maxi