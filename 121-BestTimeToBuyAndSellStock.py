class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if prices==sorted(prices, reverse=True):
        #     return 0

        # maxDiff=0
        # for index1 in range(len(prices)-1):
        #     for index2 in range(index1+1, len(prices)-1):
        #         maxDiff = max(maxDiff, prices[index2]-prices[index1])

        # # print(maxDiff)
        # return maxDiff

        max_profit=0
        min_price=prices[0]

        for price in prices:
            max_profit=max(max_profit, price-min_price)
            min_price=min(min_price, price)
        
        return max_profit
