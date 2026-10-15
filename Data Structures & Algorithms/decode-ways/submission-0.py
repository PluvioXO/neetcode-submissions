class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i) -> int:
            if i >= len(s):
                return 1
            elif i+1 >= len(s):
                if s[i] != "0":
                    return 1
            if s[i] == "0":
                return 0
            else:
                if int(s[i:i+2]) < 27:
                    return dp(i+1)+dp(i+2)
                else:
                    return dp(i+1)
        return dp(0)