class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        a = set(nums)

        for x in a:
            temp = 1
            if x-1 not in a: 
                t = x+1
                while t in a:
                    temp += 1
                    t+= 1
                longest = max(temp, longest)
        return longest