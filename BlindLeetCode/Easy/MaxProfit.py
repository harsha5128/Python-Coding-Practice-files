class Solution:
    def maxProfit(self, prices) :
        res = 0   
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res 

solution=Solution()
prices=[7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))