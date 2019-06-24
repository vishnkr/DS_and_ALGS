#Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_profit=0
        for i in range(0,len(prices)):
            if min_price is None:
                min_price = prices[i]
            if prices[i]<min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit