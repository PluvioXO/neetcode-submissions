class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = len(nums2)
        while count > 0:
            nums1.pop()
            count -= 1
        ptr1, ptr2 = 0, 0 
        while ptr1 < len(nums1) and ptr2 < len(nums2): 
            print(nums1)
            if nums1[ptr1] > nums2[ptr2]:
                nums1.insert(ptr1, nums2[ptr2])
                ptr2 += 1
            else: 
                ptr1 += 1
        nums1 += nums2[ptr2:]