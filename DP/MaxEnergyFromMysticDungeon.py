'''3147. Taking Maximum Energy From the Mystic Dungeon

In a mystic dungeon, n magicians are standing in a line. 
Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k).
This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps 
until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

Example 1:
Input: energy = [5,2,-10,-5,1], k = 3

Output: 3
Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:
Input: energy = [-2,-3,-1], k = 2

Output: -1
Explanation: We can gain a total energy of -1 by starting from magician 2.
'''
class Solution(object):
    def maximumEnergy(self, A, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        '''r={}
        for i in range(len(energy),k):
            if energy[i+k]>=0 or energy[k]<0:
                r[[energy[i],energy[i+k]]]= energy[i]+energy[i+k]
            else:
                for i in range(len(energy)-k,len(energy)):
                    r[energy[i]]=energy[i]
        m=max(r.values())
        return m'''
        for i in range(len(A) - k - 1, -1, -1):
            A[i] += A[i + k]
        return max(A)

            
            

            
