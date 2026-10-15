class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        rob1a, rob2a = 0, 0
        rob1b, rob2b = 0, 0
        for n in range(len(nums)-1):
            tempa = max(rob1a+nums[n+1], rob2a)
            rob1a = rob2a
            rob2a = tempa 

        for n in range(len(nums)-1):
            tempb = max(rob1b+nums[n], rob2b)
            rob1b = rob2b
            rob2b = tempb 
        return max(rob1a,rob2a,rob1b,rob2b)