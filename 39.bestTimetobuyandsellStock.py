class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price=prices[0]
        maximum_profit=0
        for i in prices[1:]:
            maximum_profit=max(maximum_profit,i-minimum_price)
            minimum_price=min(i,minimum_price)
        return maximum_profit