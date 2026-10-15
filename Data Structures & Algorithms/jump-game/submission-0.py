class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True 
        goal  = len(nums) - 1
        pointer = goal - 1 
        while pointer >= 0: 
            if nums[pointer] >= goal - pointer:
                goal = pointer 
            pointer -= 1 
            if goal == 0:
                return True

        return False 