class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) # we reduce the need to do pointless computation 
        while k > 0: 
            item = nums.pop()
            nums.insert(0, item)
            k -= 1