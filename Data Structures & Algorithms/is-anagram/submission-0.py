class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c1={}
        c2={}

        for i in s:
            if i in c1:
                c1[i]+=1
            else:
                c1[i]=1
        for i in t:
            if i in c2:
                c2[i]+=1
            else:
                c2[i]=1
        if c1==c2:
            return True
        else:
            return False
        