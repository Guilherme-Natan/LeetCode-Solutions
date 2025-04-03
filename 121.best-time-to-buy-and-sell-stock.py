#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit


# @lc code=end
