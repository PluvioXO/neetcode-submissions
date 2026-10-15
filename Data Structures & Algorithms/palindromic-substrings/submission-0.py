class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        total = len(s) 
        for i in range(len(s)-2):
            l = i 
            r = i + 2
            while l > -1 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1 
                r += 1
        for i in range(len(s)-1):
            l = i 
            r = i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        return total; 
