class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price-least_price)
            least_price = min(least_price, price)
        return max_profit
        