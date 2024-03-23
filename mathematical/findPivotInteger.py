'''2485. Find the Pivot Integer
Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.


#my soln , 2349ms 
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        else:
            x=n/2
            while x<=n:
                l=[]
                r=[]
                for i in range(1,x+1):
                    l.append(i)
                for i in range(x,n+1):
                    r.append(i)
                if sum(l)==sum(r):
                    break
                else:
                    x+=1
            if x<=n:
                return x
            else:
                return -1'''
# 12ms 
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=sqrt(n*(n+1)//2)
        return -1 if x%1!=0 else int(x)
        
                
                        
        
