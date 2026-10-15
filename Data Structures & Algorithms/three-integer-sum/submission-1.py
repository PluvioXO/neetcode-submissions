class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] + nums[1] + nums[2] == 0:
            return [[nums[0], nums[1], nums[2]]]
        ans = [] 
        for i in range(len(nums) - 2):
            if nums[i] > 0: 
                return ans
            if nums[i] == nums[i-1]:
                continue
            lp = i + 1 
            rp = len(nums)-1
            while rp > lp: 
                total = nums[i] + nums[lp] + nums[rp]
                if total > 0:
                    rp -= 1
                elif total < 0:
                    lp += 1 
                else:
                    anstoappend = [nums[i], nums[lp], nums[rp]]
                    ans.append(anstoappend)
                    lp += 1
                    rp -= 1

                    while nums[lp] == nums[lp - 1] and lp < rp:
                        lp += 1
                    while nums[rp] == nums[rp + 1]:
                        rp -= 1
        return ans



