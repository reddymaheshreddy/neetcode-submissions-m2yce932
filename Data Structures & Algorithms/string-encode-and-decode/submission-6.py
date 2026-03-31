class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res+=str(len(word))+":"+word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            index=s.find(':',i)
            val=int(s[i:index])
            res.append(s[index+1:index+1+val])
            i=index+1+val
        return res

