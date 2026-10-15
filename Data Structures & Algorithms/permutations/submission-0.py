class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        def dfs(arr: List[int], numsPerm: List[int]) -> None:
            nonlocal ans 
            if len(numsPerm) == 0:
                ans.append(arr)
            for i in range(len(numsPerm)):
                a = numsPerm.copy()
                a.pop(i)
                dfs(arr+[numsPerm[i]], a)
        dfs([], nums)
        return ans 
            