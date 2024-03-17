'''100248. Existence of a Substring in a String and Its Reverse
User Accepted:10865
User Tried:11808
Total Accepted:11082
Total Submissions:15844
Difficulty:Easy

Given a string s, find any substring of length 2 which is also present in the reverse of s.
Return true if such a substring exists, and false otherwise.

Example 1:
Input: s = "leetcode"
Output: true
Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

Example 2:
Input: s = "abcba"
Output: true
Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

Example 3:
Input: s = "abcd"
Output: false
Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters.'''

#my soln , accepted!
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp=""
        t=s
        for i in range(1,len(t)):
            temp=t[i-1]+t[i]
            if temp in t:
                if temp in t[::-1]:
                    return True
        return False
        
