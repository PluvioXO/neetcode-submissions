class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtab = set() 
        for x in nums:
            if x not in hashtab:
                hashtab.add(x)
            else:
                return True
        return False