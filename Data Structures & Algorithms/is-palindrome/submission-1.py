class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lp = 0
        rp = len(s) - 1 
        while lp < rp: 
            while not s[lp].isalnum() and lp < rp: 
                lp += 1
            while not s[rp].isalnum() and lp < rp:
                rp -= 1
            
            if s[lp] != s[rp]:
                return False

            lp += 1
            rp -= 1
            
        return True