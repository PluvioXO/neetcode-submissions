class Solution:
    def hammingWeight(self, n: int) -> int:
        def int2str(n: int) -> str:
            s = ""
            exp = 31
            while exp > -1:
                if n - (2**exp) > -1: 
                    n -= 2**exp
                    s += "1"
                else:
                    s += "0"
                exp -= 1
            return s
        sum = 0
        string = int2str(n)
        print(string)
        for i in string:
            if i == "1":
                sum += 1  
        return sum