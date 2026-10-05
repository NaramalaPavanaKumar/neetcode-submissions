class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str1=""
        str2=""
        i=len(s)-1
        while i>=0:
            if s[i].isalnum():
                str2=str2+s[i]
            i-=1
        i=0
        while i<len(s):
            if s[i].isalnum():
                str1=str1+s[i]
            i+=1
        
        if str1==str2:
            return True
        else:
            return False
        