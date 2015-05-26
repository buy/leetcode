# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0

        low, maxDiff = prices[0], 0
        for price in prices[1:]:
            if price < low:
                low = price
            else:
                diff = price - low
                if diff > maxDiff:
                    maxDiff = diff

        return maxDiff
