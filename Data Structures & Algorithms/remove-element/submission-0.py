class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = len(nums)-1
        while ptr > -1: 
            if nums[ptr] == val: 
                nums.pop(ptr)
            ptr -= 1 
        return len(nums)
        