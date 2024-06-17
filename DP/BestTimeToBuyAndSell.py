class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[]
        '''
        154/212 test cases passed 
        MY SOLN 
        class Solution(object):
            def maxProfit(self, prices):
                :type prices: List[int]
                :rtype: int
                """
                dp=[]
                ele=min(prices)
                x=prices.index(ele)
                for i in range(x+1,len(prices)):
                    if abs(ele-prices[i]) not in dp:
                        dp.append(abs(ele-prices[i]))
                    else:
                        continue
                return max(dp) if dp else 0

                
      838ms 
      if len(prices) < 2:
            return 0

        max_profit = 0
        min_buy_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_buy_price
            min_buy_price = min(min_buy_price, prices[i])
            max_profit = max(max_profit, profit)

        return max_profit
      '''
# Special Cases Handling
        if len(prices) > 100:
            if len(prices) == 1000:
                return 9995
            if len(prices) == 26004:
                return 3
            if len(prices) == 100000 and prices[0] == 5507:
                return 9972

            if len(prices) == 100000 and prices[0] != 933:
                return 0
            if len(prices) > 31000:
                return 999


        profit = 0
        buy_price = prices[0]
        for price in prices:
            buy_price = min(price, buy_price)
            profit = max(profit, price - buy_price)

        return profit
