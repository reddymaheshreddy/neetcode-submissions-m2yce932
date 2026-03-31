class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        for ch in s:
            if ch in dict1:
                dict1[f"{ch}"]+=1
            else:
                dict1[f"{ch}"]=1
        dict2={}
        for ch in t:
            if ch in dict2:
                dict2[f"{ch}"]+=1
            else:
                dict2[f"{ch}"]=1
        if dict1==dict2:
            return True
        else:
            return False
        