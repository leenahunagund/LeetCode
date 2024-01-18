'''70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

FIBONACCI
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:return 0
        if n==1:return 1
        if n==2:return 2

        one_step_before=2
        two_step_before=1
        total_ways=0

        for i in range(2,n):
            total_ways=one_step_before+two_step_before
            two_step_before=one_step_before
            one_step_before=total_ways
        return total_ways
    
                

        
