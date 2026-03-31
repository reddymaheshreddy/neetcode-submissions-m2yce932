class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len (board)
        cols = len(board[0])
        n = len (word)
        visited = set()
        def backtrack(r,c,i):
            if i == n :
                return True
            res = False
            visited.add((r,c))
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                if 0<= r + dr < rows and 0<= c + dc < cols and board[r+dr][c+dc] == word[i] and (r+dr,c+dc) not in visited:
                    
                    res = res or backtrack(r+dr,c+dc,i+1)
            visited.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                   if backtrack(r,c,1):
                    return True
        return False

            