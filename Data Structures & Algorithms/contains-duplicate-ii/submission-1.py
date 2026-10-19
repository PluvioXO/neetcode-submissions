class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} 
        for idx, item in enumerate(nums): 
            if item in seen and abs(seen[item] - idx) <= k:
                return True
            else: 
                seen[item] = idx
        return False;