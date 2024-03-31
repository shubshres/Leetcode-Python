class Solution:
    def maxProfit(self, prices):
        l = 0
        profit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r

        return profit


# driver function
print(Solution.maxProfit(Solution, [7, 1, 5, 3, 6, 4])) # 5

# Time complexity: O(n)
# Space complexity: O(1)