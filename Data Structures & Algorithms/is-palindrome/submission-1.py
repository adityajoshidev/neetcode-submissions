class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x for x in s.lower() if x in '0123456789abcdefghijklmnopqrstuvwxyz']
        i=0
        j=-1
        while i<len(s):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True