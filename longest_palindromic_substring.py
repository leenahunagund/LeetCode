'''5. Longest Palindromic Substring
Medium
28.3K
1.7K
Companies
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb" 

--my soln-- 
62/102 test cases passed '''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=[]
        a=[]
        k=""
        r=""
        n=len(s)
        c=s[::-1]
        for i in range(n):
            if s[i]==c[i]:
                a.append(s[i])
        
        k=k.join(a)
        r=r.join(k[::-1])
        if k==r:
            return k



            
            



 
