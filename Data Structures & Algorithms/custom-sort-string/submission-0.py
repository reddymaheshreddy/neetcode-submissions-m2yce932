class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        res=""
        for ch in order:
            if ch in freq:
                res+= ch*freq[ch]
                del freq[ch]
        for ch in s :
            if ch in freq:
                res+=ch
        return res

        