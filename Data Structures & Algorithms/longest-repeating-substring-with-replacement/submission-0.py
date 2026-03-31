class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        count = {}
        res = 0
        i=0
        maxRepeat=0
        for j in range(n):
            count[s[j]]=1+count.get(s[j],0)
            maxRepeat=max(maxRepeat,count[s[j]])
            while (j-i+1) - maxRepeat > k:
                count[s[i]]-=1
                i+=1
            res = max(res,j-i+1)
        return res
        