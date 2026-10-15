class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        if len(s) == 2 and s[0] != s[-1]:
            return s[0]
        ans = ""
        for i in range(len(s)-2):
            l = i
            r = i + 2
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            ans = s[l+1: r] if len(s[l+1:r]) > len(ans) else ans
        for i in range(len(s)-1):
            l = i
            r = i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            ans = s[l+1: r] if len(s[l+1:r]) > len(ans) else ans
            
        return ans