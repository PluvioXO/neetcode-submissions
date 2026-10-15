from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = Counter()
        l, r = 0, 0 
        ans = 0
        chars[s[r]] += 1
        while r != len(s)-1:
            r += 1 
            # Add new item to char
            chars[s[r]] += 1
            print(l,r, chars.most_common(1)[0][1]+k, r-l+1)
            if chars.most_common(1)[0][1] + k < r-l+1:
                chars[s[l]] -= 1
                l += 1
            if r-l+1 > ans: 
                ans = r-l+1
        return ans 

            