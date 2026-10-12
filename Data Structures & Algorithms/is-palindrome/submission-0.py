class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=0
        s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(s)):
            if s[i] == s[len(s)-1-i]:
                x=x+1
        if x == len(s): 
            return True
        return False