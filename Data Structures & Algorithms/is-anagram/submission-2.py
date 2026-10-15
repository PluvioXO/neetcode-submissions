class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1 = {} 
        for x in s:
            if x not in hashMap1:
                hashMap1[x] = 1
            else:
                hashMap1[x] += 1
        for x in t:
            if x not in hashMap1:
                return False
            else:
                hashMap1[x] -= 1
                if hashMap1[x] < 0: 
                    return False
        return True
        