class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0 

        for num in numSet:
            if num-1 not in numSet:
                c = 1
                while num+c in numSet:
                    c += 1
                res = max(res, c)
        return res; 