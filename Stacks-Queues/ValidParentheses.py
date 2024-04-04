'''20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''c=0       my code 77/98 test cases
        for i in s:
            if i=='(' or i=='[' or i=='{':
                c+=1
            if (i==')' and '(' in s):
                c-=1
            if (i==']' and '[' in s):
                c-=1 
            if (i=='}' and '{' in s):
                c-=1
        return c==0'''
        stack = []
        o = {"(": ")", "{": "}", "[": "]"}

        for i in s:
            if i in o:  # Check for opening brackets
                stack.append(i)
            elif len(stack) == 0 or o[stack.pop()] != i:  # Check for matching closing brackets 
                return False

        return len(stack) == 0

        
