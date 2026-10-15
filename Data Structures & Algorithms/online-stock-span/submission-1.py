class StockSpanner:

    def __init__(self):
        self.history = [] 

    def next(self, price: int) -> int:
        self.history.append(price)
        local = self.history.copy()
        total = 1
        while len(local) > 1:
            current = local.pop()
            prev_day = local.pop()
            if current >= prev_day:
                total += 1
                local.append(current)
            else:
                return total
        return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)