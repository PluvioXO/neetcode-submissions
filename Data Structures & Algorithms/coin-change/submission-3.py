class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {}
        def dp(x: int) -> int: 
            if x in seen:
                return seen[x]
            if x == 0: 
                return 0
            if x > 0:
                valid_items = [c for c in coins if c <= x] 
                if len(valid_items) > 0:
                    seen[x] = min([(1 + dp(x-i)) for i in valid_items])
                    return seen[x]
                return float('inf')
        ans = dp(amount)
        return(ans) if ans != float('inf') else -1 
        

