class Solution:
    def isPalindrome(self, s: str) -> bool:
        for ch in s:
            if not ch.isalnum():
                s=s.replace(ch,'')
        s=s.lower()
        st=0
        en=len(s)-1
        while st<en:
            if s[st] != s[en]:
                return False
            st+=1
            en-=1
        return True