'''387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for l in s:
            if l not in d:
                d[l]=1
            else:
                d[l]+=1
            
        index=-1
        for i in range(len(s)):
            if d[s[i]]==1:
                index=i
                break
        return index

        
        
