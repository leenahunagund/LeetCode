'''1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
  
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
  
Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
  
Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

----my soln--- 11/47 cases passed
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def check(text1, text2):
            count=0
            for i in range((len(text1)-len(text2))+1):
                for j in range(len(text2)):
                    if text1[i+j]==text2[j]:
                        count+=1
            return count
        x=0
        if len(text1)>=len(text2):
            x=check(text1,text2)
            return x
        else:
            if len(text1)<len(text1):
                x=check(text2,text1) 
            return x
       '''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        
        text1 = " " + text1
        text2 = " " + text2
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[-1][-1]
       
               
               
