class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        
        n = len(digits)
        def backtrack(i,temp):
            if i == n:
                res.append(temp)
                return
            for letter in combinations[int(digits[i])-2]:
                backtrack(i+1,temp+letter)
        backtrack(0,"")
        return res
