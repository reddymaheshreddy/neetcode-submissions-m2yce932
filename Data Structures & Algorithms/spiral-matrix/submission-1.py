class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        row = len(matrix)
        col = len(matrix[0])
        def spiral(i,j,k):
            res.append(matrix[i][j])
            visited.add((i,j))
            ds =[[0,1],[1,0],[0,-1],[-1,0]]
            for m in range(4):
                ind  = (k+m)%4
                x,y = ds[ind][0]+i,ds[ind][1]+j
                if (x,y) not in visited and 0<=x<row and 0<=y<col:
                    
                    return spiral(x,y,ind)
        spiral(0,0,0)
        return res

        

        