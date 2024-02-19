'''231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

979 test cases/1109
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        if t==1:
            return True
        else:
            while t>0:
                t=t/2
                t-=2
                if t==1:
                    break
            return t==1 and n%2==0

passed all 1109 testcases 19ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(32):
            if pow(2,i)==n:
                return True
        return False'''

#passed all 1109, 10ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result=0
        i=0
        while(True):
            result=2**i
            if result==n:
                return True
            elif result>n:
                return False
            i+=1
            
            



        


                  



        
