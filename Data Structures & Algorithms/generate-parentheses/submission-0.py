class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(open,close,temp):
            if open == n and close == n:
                res.append(temp)
                return
            if open == n :
                
                backtrack(open,close+1,temp+")")
            elif open == close:
              
                backtrack(open+1,close,temp+"(")
            else:
                backtrack(open+1,close,temp+"(")
                backtrack(open,close+1,temp+")")
        backtrack(0,0,"")
        return res
            

        