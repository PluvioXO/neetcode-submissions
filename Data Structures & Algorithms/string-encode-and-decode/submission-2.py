class Solution:

    def encode(self, strs: List[str]) -> str:
        c = 0 
        for i in range(len(strs)):
            strs.insert(c, "{:4}".format(len(strs[c])))
            c += 2 
        return("".join(strs))
    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0 
        while i < len(s): 
            temp = ""
            for _ in range(4):
                temp += s[i]
                i += 1
            temp = int(temp)
            ans.append(s[i:i+temp])
            i += temp
        return ans 
