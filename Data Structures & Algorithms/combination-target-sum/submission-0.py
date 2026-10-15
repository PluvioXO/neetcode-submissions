from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        ans = [] 
        def dfs(x: int, item):
            if x < 0:
                return 
            if x == 0:
                item.sort()
                if str(item) not in seen:
                    seen.add(str(item))
                    ans.append(item)
                return 
            [dfs(x-i, [i]+item) for i in nums]
        dfs(target, [])
        return ans