class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lArray = [nums[0]] 
        rArray = [nums[-1]]

        #Left moving array
        for x in range(1, len(nums), 1):
            lArray.append(lArray[-1]*nums[x])

        for y in range(len(nums)-2, -1, -1):
            rArray.append(rArray[-1]*nums[y])

        ans = [rArray[len(nums)-2]] 
        for i in range(len(nums)-2):
            ans.append(lArray[i]*rArray[len(nums)-3-i])
        ans.append(lArray[len(nums)-2])
        return ans 