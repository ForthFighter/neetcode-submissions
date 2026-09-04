class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best_profit = 0

        for day in range(len(prices)-1):
            future = prices[day + 1 :]
            best_future_price = max(future)
            best_profit = max(0,best_profit,best_future_price - prices[day])

        return best_profit
        