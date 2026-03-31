class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr =[]
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i,total):
            if total == target:
                res.append(curr[:])
                return 
            if i >= n:
                return 
            for j in range(i,n):
                if j> i  and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    return 
                curr.append(candidates[j])
                backtrack(j+1,total + candidates[j])
                curr.pop()
        backtrack(0,0)
        return res
        