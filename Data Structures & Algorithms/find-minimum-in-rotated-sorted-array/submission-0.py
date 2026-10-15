class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums)-1
        while lp < rp: 
            mid = (lp + rp)//2
            if nums[mid] > nums[rp]:
                lp = mid + 1 
            elif nums[mid] < nums[rp]:
                rp = mid 
        return nums[lp]