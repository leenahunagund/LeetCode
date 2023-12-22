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
Output: "bb" '''

class Solution:
    def longestPalindrome(self, s):
        ans=''
        for i in range(len(s)):
            ans=max(ans,expand(s,i,i), expand(s,i,i+1), key=len)
        return ans
            
def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j]
    
'''--my soln-- 
66/142 test cases passed 
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
            elif c[i-1]==c[i]:
                a.append(c[i])
            else:
                if s[i-1]==s[i]:
                    a.append(s[i])
            
        if not a:
            return s[0]
        k=k.join(a)
        r=r.join(k[::-1])
        if k==r:
            return k
'''

            
            






            
            



 
