class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = (None, 0)
        items = {} 
        for char in nums: 
            if char not in items:
                items[char] = 0
            items[char] += 1 
            if items[char] > ans[1]:
                ans = (char, items[char])
        return ans[0]