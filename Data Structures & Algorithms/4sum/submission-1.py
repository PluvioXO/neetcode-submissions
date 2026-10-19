class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #print(nums)
        solution = set()
        a = 0 
        solutions = [] 
        while a < len(nums)-3: 
            b,c,d = a+1, a+2, a+3
            total = sum([nums[a], nums[b], nums[c], nums[d]])
            if total > target:
                return solutions
            while b < len(nums)-2: 
                c = b+1
                d = len(nums)-1
                while c<d: 
                    total = sum([nums[a], nums[b], nums[c], nums[d]])
                    #print(total, a,b,c,d)
                    if total == target and str([nums[a],nums[b],nums[c],nums[d]]) not in solution: 
                        solutions.append([nums[a],nums[b],nums[c],nums[d]])
                        solution.add(str([nums[a],nums[b],nums[c],nums[d]]))
                    elif total > target: 
                        d -= 1
                    else:
                        c += 1
                b += 1
            a += 1
        return solutions 