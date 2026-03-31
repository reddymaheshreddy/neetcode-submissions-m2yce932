class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos = set()
        neg = set()
        res = []
        temp = []
        for i in range(n):
            row = ["."]*n
            temp.append(row)
        
        def backtrack(i):
            if i == n:
                final = []
                for r in temp:
                    final.append("".join(r))
                res.append(final[:])

                return 
            for j in range(n):
                if j not in cols and (j-i) not in neg and (i+j) not in pos:
                    cols.add(j)
                    neg.add(j-i)
                    pos.add(i+j)
                    temp[i][j] = "Q"
                    backtrack(i+1)
                    cols.remove(j)
                    neg.remove(j-i)
                    pos.remove(i+j)
                    temp[i][j] = "."
        backtrack(0)
        return res




        