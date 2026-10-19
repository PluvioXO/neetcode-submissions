class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # you can start at idx 0 or 1, and go up 1 or 2 steps at each position. 
        ans = {}
        ans[len(cost)-1] = cost[len(cost)-1]
        ans[len(cost)-2] = cost[len(cost)-2]
        ptr = len(cost)-3
        while ptr > -1: 
            print(ptr, ans)
            ans[ptr] = cost[ptr] + min(ans[ptr+1], ans[ptr+2])
            ptr -= 1
        return min(ans[0], ans[1])
