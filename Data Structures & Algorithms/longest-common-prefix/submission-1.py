class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = "" 
        ptr = 0 
        current = strs[0]
        while ptr < len(current):
            temp = current[ptr]
            for current in strs: 
                if ptr == len(current) or current[ptr] != temp:
                    return ans; 
            ans += temp
            ptr += 1 
        return ans 