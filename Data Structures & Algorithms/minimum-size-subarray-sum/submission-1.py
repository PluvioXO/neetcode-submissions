class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0, 1
        total = nums[0]
        ans = 10**7
        while r < len(nums):
            if total >= target: 
                ans = min(ans, r-l)
                total -= nums[l]
                l += 1
            else:
                total += nums[r]
                r += 1
        while total >= target: 
            ans = min(ans, r-l)
            total -= nums[l]
            l += 1
        if ans == 10**7:
            return 0
        return ans; 