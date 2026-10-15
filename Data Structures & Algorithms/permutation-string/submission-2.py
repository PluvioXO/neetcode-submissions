class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        hashtab = {}
        l = 0 
        r = len(s1)
        for x in s1: 
            if x not in hashtab: 
                hashtab[x] = 1
            else: 
                hashtab[x] += 1
        c = len(hashtab.values()) # Init a counter of length of values in hastab. 

        for x in range(len(s1)): 
            if s2[x] in hashtab: 
                hashtab[s2[x]] -= 1 
                if hashtab[s2[x]] == 0: 
                    c -= 1
        if c == 0:
            return True
        
        while r < len(s2):
            print(hashtab, l, r)
            if s2[l] in hashtab: 
                hashtab[s2[l]] += 1
                if hashtab[s2[l]] == 1: 
                    c += 1 
            l += 1
            if s2[r] in hashtab: 
                hashtab[s2[r]] -= 1
                if hashtab[s2[r]] == 0: 
                    c -= 1
                if c == 0: 
                    return True
            r += 1

        return False