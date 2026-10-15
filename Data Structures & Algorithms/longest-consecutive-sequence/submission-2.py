class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        a = set(nums)

        for x in nums:
            count = 1
            if (x-1) in a: 
                t = x-1 
                while t in a:
                    count += 1
                    t -= 1
            if count > longest:
                    longest = count 
        return longest 