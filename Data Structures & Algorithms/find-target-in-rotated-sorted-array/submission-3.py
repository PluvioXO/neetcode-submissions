class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return the ptr to the target else -1

        # we can partition the array into 2 sorted sections around pivot. 
        # we need to first find the pivot point which is max(nums)

        l,r = 0, len(nums)-1
        mid = (l+r) // 2
        if nums[mid] < nums[l]: 
            if target == nums[l]:
                return l
            elif target > nums[l]:
                r = mid - 1 
        elif nums[mid] > nums[r]:
            if target == nums[r]:
                return r
            elif target < nums[r]:
                l = mid + 1 
            
        # target exists between index l and r
        while l<=r:
            mid = (l + r) // 2
            if nums[l] == target:
                return l 
            if nums[r] == target:
                return r
            if nums[mid] == target: 
                return mid 
            if nums[mid] > target:
                r = mid - 1 
            elif nums[mid] < target: 
                l = mid + 1  
        print(l,r,mid)
        return -1 # we do not find it 

            