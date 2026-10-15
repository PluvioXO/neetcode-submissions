class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = {} 
        for x in nums1:
            hash1[x] = -1
        stack = [] 
        i = 0 
        while i < len(nums2): 
            print(stack )
            while len(stack) > 0 and nums2[i] > stack[-1]: 
                hash1[stack[-1]] = nums2[i]
                stack.pop()
            if nums2[i] in hash1: 
                stack.append(nums2[i])
            i += 1

        return hash1.values()