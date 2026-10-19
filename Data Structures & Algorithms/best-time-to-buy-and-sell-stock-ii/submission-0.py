class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr = 0 
        profitTotal = 0 
        position = 10**5
        while ptr < len(prices): 
            if prices[ptr] < position:
                position = prices[ptr]
            else: 
                profitTotal += (prices[ptr]-position)
                position = prices[ptr]
            ptr += 1; 
        return profitTotal;
