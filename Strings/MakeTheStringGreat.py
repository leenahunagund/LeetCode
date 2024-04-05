'''1544. Make The String Great
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"#

#9ms
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        def checkletter(c,d):
            if d==c.upper() or c==d.upper():
                return True
            else:
                return False
        l=0
        r=1
        while r<len(s):
            if checkletter(s[l],s[r]) and s[l]!=s[r]:
                s=s[:l]+s[r+1:]
                l=0
                r=1
            else:
                l+=1
                r+=1
        return s'''
#18ms
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for char in s:
            if stack and abs(ord(char)-ord(stack[-1]))==32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)




            

        
