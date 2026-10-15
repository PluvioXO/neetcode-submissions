class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        ans = 0
        temp = 0
        l = 0
        r = 0 
        while r < len(s):
            if s[r] not in a:
                a.add(s[r])
                temp += 1
                r+= 1
            else:
                ans = max(temp, ans)
                while s[l] != s[r]:
                    temp -= 1
                    a.remove(s[l])
                    l += 1
                temp -= 1
                a.remove(s[l])
                l += 1
        ans = max(temp,ans)
        return ans 