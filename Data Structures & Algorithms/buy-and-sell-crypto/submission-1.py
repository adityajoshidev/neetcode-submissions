class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1,-1,-1):
            selling_price=prices[i]
            if i>0:
                x=selling_price-min(prices[:i])
                if profit<x:
                    profit=x
        return profit