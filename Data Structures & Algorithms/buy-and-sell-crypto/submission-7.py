class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = sorted(prices, reverse=True)
        if temp == prices:
            return 0
        minI, maxI, profit = 0, 1, 0
        for i in range(1, len(prices)):
            if prices[i]<prices[minI] and i<(len(prices)-1):
                minI = i
                maxI = i
            elif prices[i]>prices[maxI] and minI<i:
                maxI = i
            profit = max(profit, prices[maxI]-prices[minI])
        return max(profit, prices[maxI]-prices[minI])
        

            
        
        
        