class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        t=[]             #without DP, 21ms , 28/65 test cases passed,doesnt work for when a larger ord() variable is present first and the subsequent 
                                                letters hv smaller ord()
        s=sorted(list(s))
        x=ord(s[0])
        for i in range(1,len(s)):
            if abs(x-ord(s[i]))<=k:
                t.append(x)
                x=ord(s[i])
                if i==len(s)-1:
                    t.append(s[i])
            elif x<ord(s[i]) and x!=ord(s[i]):
                x=ord(s[i])
        return len(t)
        """
        dp = [0] * 128        #15ms , beats 100% users with python
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)
                

        
