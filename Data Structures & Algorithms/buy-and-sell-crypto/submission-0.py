class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profit_list = []
        for i in range(len(prices)):
            step = 1
            while step+i < len(prices):
                if prices[i+step]>prices[i]:
                    diff = prices[i+step] - prices[i]
                    profit_list.append(diff)
                step +=1
        if not profit_list:
            return 0
        else:
            profit = max(profit_list)
        return profit

         
