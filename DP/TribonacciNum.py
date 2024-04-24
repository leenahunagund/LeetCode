class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        
        def rec(n): #with Recursion: 230ms
            if n==0: return 0
            if n==1 or n==2: return 1
            return rec(n-3)+rec(n-2)+rec(n-1)
        return rec(num)     """
      
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        def dp( i ):      #dp:10ms
            if i in memo:
                return memo[i]
            memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
            return memo[i]
        return dp(n)
