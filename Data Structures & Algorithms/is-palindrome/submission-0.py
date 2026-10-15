class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "" 
        for x in s:
            if isinstance(x, str) and (x.lower() >= 'a' and x.lower() <='z'):
                clean += x.lower()
            elif x >= '0' and x <= '9':
                clean += x
        lp = 0 
        rp = len(clean) - 1 
        while lp < rp:
            if clean[lp] != clean[rp]:
                return False
            lp += 1
            rp -= 1
        return True