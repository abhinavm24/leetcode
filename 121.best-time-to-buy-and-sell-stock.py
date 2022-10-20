#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (54.48%)
# Likes:    20694
# Dislikes: 662
# Total Accepted:    2.7M
# Total Submissions: 5M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
# 
# 
# Example 1:
# 
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
# 
# 
# Example 2:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n*n, 1
        # maxProfit = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j]-prices[i])
        # return maxProfit


        # n, 1
        # next 3 solutions are same approach
        maxProfit = 0
        best_price_to_buy = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - best_price_to_buy)
            best_price_to_buy = min(best_price_to_buy, prices[i])
        return maxProfit



        # buy_price = prices[0] # at the begining the minimum price is the first price
        # profit = 0 # at the begining the minimum  profit is zero
        
        # for i in range(1,len(prices)):
        #     #if the current price is less than the previous buy price ; update the buy_price
        #     if prices[i] < buy_price:
        #         buy_price = prices[i]
        #     else: # if not check if you sell with the current price would you get better profit than the previous one
        #         profit = max(profit, prices[i]-buy_price) # compare the previous profit with the current profit
        # return profit



        # left = 0 #Buy
        # right = 1 #Sell
        # maxProfit = 0
        # while right < len(prices):
        #     currProfit = prices[right] - prices[left] 
        #     # left stay at min price and is only moved is smaller price is found
        #     if currProfit < 0:
        #         left = right
        #     else:
        #     # calculate profit if price higher than existing min
        #         maxProfit = max(maxProfit, currProfit)
        #         # left += 1
        #     right += 1
        # return maxProfit


        # cumulative sum if positive continuously or set to 0
        # ans = 0
        # curSum = 0
        # for i in range(len(prices)-1):
        #     curSum += prices[i+1] - prices[i]
        #     if curSum < 0:
        #         curSum = 0
        #     ans = max(ans, curSum)
        # return ans


        # Track the minimum_price and the maximum profit together using a dp table
        # Thus each dp table cell will hold two items --> dp = [[min_price, max_profit], [min_price, max_profit], ........[min_price, max_profit]]
        n = len(prices)
        dp = [0]*n # initializing the dp table
        dp[0] = [prices[0],0] # filling the the first dp table --> low_price = prices[0] max_profit=0
        min_price = max_profit = 0
        # Note that ---> indixing the dp table --> dp[i-1][0] stores minimum price and dp[i-1][1] stores maximum profit
        for i in range(1,n):
            min_price = min(dp[i-1][0], prices[i]) # min(previous_min_price, cur_min_price)
            max_profit = max(dp[i-1][1], prices[i]-dp[i-1][0]) # max(previoius_max_profit, current_profit)
            dp[i] =[min_price,max_profit]
                
        return dp[n-1][1]

# @lc code=end

