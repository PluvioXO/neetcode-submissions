class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we hold the maximum and the minimum product at the same time; 
        ans = -10**8
        ptr = 0 
        maxProd, minProd = 1, 1
        while ptr < len(nums): 
            old = maxProd
            maxProd = max([maxProd*nums[ptr], minProd*nums[ptr], nums[ptr]])
            minProd = min([old*nums[ptr], minProd*nums[ptr], nums[ptr]])
            ans = max(ans, maxProd)
            ptr += 1
            #print(ans, maxProd, minProd)
        return ans; 