class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[s for s in s.lower() if s in '0123456789abcdefghijklmnopqrstuvwxyz']
        i=s.copy()
        s.reverse()
        if s==i:
            return True
        else:
            return False