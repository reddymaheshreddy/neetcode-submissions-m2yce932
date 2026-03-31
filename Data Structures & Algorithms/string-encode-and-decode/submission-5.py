class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for st in strs:
            res=res+f'{len(st)}:{st}'
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=s.find(':',i)
            l=int(s[i:j])
            res.append(s[j+1:j+l+1])
            i=j+l+1
        return res
